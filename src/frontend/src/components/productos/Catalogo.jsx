import React, { useState, useEffect } from 'react';
import api from '../../services/api.js';
import { axiosInstance } from '../../services/api';
import CategoryService from '../../services/categoryService';
import '../styles/Catalogo.css'; // Assuming styling or I'll use inline styles for now

function Catalogo() {
  const [viewMode, setViewMode] = useState('categories'); // 'categories' | 'products'
  const [categorias, setCategorias] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  const [productos, setProductos] = useState([]);
  const [productosFiltrados, setProductosFiltrados] = useState([]);
  const [carrito, setCarrito] = useState([]);
  const [tiendaId, setTiendaId] = useState(1);
  const [secciones, setSecciones] = useState([]);

  // Filtros products
  const [filtros, setFiltros] = useState({
    busqueda: '',
    seccion: '',
    precioMin: '',
    precioMax: '',
    ordenPrecio: 'none',
    mostrarBasicos: false
  });

  const token = localStorage.getItem('token');

  // Load Categories on Mount
  useEffect(() => {
    const fetchCats = async () => {
        try {
            const data = await CategoryService.getAll();
            setCategorias(Array.isArray(data) ? data : []);
        } catch (e) {
            console.error("Error fetching categories:", e);
        }
    };
    fetchCats();
    cargarSecciones();
  }, []);

  // Load Products when category is selected
  useEffect(() => {
      if (selectedCategory) {
          cargarProductos();
      }
  }, [selectedCategory, tiendaId]);

  // Apply filters when products loaded or filters change
  useEffect(() => {
    aplicarFiltros();
  }, [productos, filtros, secciones]);


  const cargarSecciones = async () => {
    try {
      const res = await axiosInstance.get('/productos/secciones/');
      const data = res.data.results || res.data;
      setSecciones(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error('Error cargando secciones:', err);
    }
  };

  const cargarProductos = async () => {
    try {
        // Ideally fetch by category filtered in backend: /productos/?categoria=NAME
        // But for now, fetch all or store-based and filter client side, or if API supports it.
        // The current API: api.getProductos returns all.
        let data = await api.getProductos(token); // Or getProductosPorTienda if logic requires
        // Filter by category strict
        if (selectedCategory) {
            data = data.filter(p => p.categoria === selectedCategory.nombre);
        }
        setProductos(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error('Error cargando productos:', err);
      setProductos([]);
    }
  };

  const aplicarFiltros = () => {
    let filtrados = [...productos];

    if (filtros.busqueda) {
      filtrados = filtrados.filter(p =>
        p.nombre.toLowerCase().includes(filtros.busqueda.toLowerCase())
      );
    }
    // Note: Category filter is already applied by 'selectedCategory' state logic, 
    // but we can keep it if we want sub-filtering (though UI flow says strict hierarchy).

    if (filtros.seccion) {
      const seccionSeleccionada = secciones.find(s => s.id === parseInt(filtros.seccion));
      if (seccionSeleccionada && seccionSeleccionada.productos) {
        filtrados = filtrados.filter(p => seccionSeleccionada.productos.includes(p.id));
      }
    }
    if (filtros.precioMin) {
      filtrados = filtrados.filter(p => parseFloat(p.precio) >= parseFloat(filtros.precioMin));
    }
    if (filtros.precioMax) {
      filtrados = filtrados.filter(p => parseFloat(p.precio) <= parseFloat(filtros.precioMax));
    }
    if (filtros.mostrarBasicos) {
      filtrados = filtrados.filter(p => p.es_basico === true);
    }
    if (filtros.ordenPrecio === 'asc') {
      filtrados.sort((a, b) => a.precio - b.precio);
    } else if (filtros.ordenPrecio === 'desc') {
      filtrados.sort((a, b) => b.precio - a.precio);
    }

    setProductosFiltrados(filtrados);
  };

  const agregarAlCarrito = (producto) => {
    const existe = carrito.find(p => p.id === producto.id);
    if (existe) {
      setCarrito(carrito.map(p =>
        p.id === producto.id ? { ...p, cantidad: p.cantidad + 1 } : p
      ));
    } else {
      setCarrito([...carrito, { ...producto, cantidad: 1 }]);
    }
  };

  const handleCategorySelect = (cat) => {
      setSelectedCategory(cat);
      setViewMode('products');
  };

  const handleBackToCategories = () => {
      setSelectedCategory(null);
      setViewMode('categories');
      setProductos([]); // Clear products to avoid flash
  };

  const limpiarFiltros = () => {
    setFiltros({
      busqueda: '',
      seccion: '',
      precioMin: '',
      precioMax: '',
      ordenPrecio: 'none',
      mostrarBasicos: false
    });
  };

  // RENDER
  if (viewMode === 'categories') {
      return (
          <div className="catalogo">
              <h1 className="catalogo-title">Explora por Categoría</h1>
              <p className="catalogo-subtitle">Selecciona una categoría para ver los productos disponibles</p>
              
              <div className="categories-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '20px', padding: '20px' }}>
                  {categorias.map(cat => (
                      <div 
                        key={cat.id} 
                        className="category-card" 
                        onClick={() => handleCategorySelect(cat)}
                        style={{
                            border: '1px solid #e2e8f0',
                            borderRadius: '12px',
                            cursor: 'pointer',
                            overflow: 'hidden',
                            transition: 'transform 0.2s, box-shadow 0.2s',
                            background: 'white',
                            textAlign: 'center',
                            boxShadow: '0 4px 6px rgba(0,0,0,0.05)'
                        }}
                        onMouseEnter={(e) => {
                           e.currentTarget.style.transform = 'translateY(-5px)';
                           e.currentTarget.style.boxShadow = '0 10px 15px rgba(0,0,0,0.1)';
                        }}
                        onMouseLeave={(e) => {
                           e.currentTarget.style.transform = 'translateY(0)';
                           e.currentTarget.style.boxShadow = '0 4px 6px rgba(0,0,0,0.05)';
                        }}
                      >
                          <div style={{ height: '150px', background: '#f8fafc', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                              {cat.imagen ? (
                                  <img src={cat.imagen} alt={cat.nombre} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                              ) : (
                                  <span style={{ fontSize: '3rem' }}>📦</span>
                              )}
                          </div>
                          <div style={{ padding: '15px' }}>
                              <h3 style={{ margin: '0 0 5px 0', fontSize: '1.2rem', color: '#1e293b' }}>{cat.nombre}</h3>
                              {cat.descripcion && <p style={{ fontSize: '0.9rem', color: '#64748b', margin: 0 }}>{cat.descripcion}</p>}
                          </div>
                      </div>
                  ))}
                  {categorias.length === 0 && (
                      <p style={{ gridColumn: '1/-1', textAlign: 'center', color: '#64748b' }}>No hay categorías disponibles.</p>
                  )}
              </div>
          </div>
      );
  }

  // View Mode: products
  return (
    <div className="catalogo">
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px', gap: '15px' }}>
          <button 
            onClick={handleBackToCategories}
            style={{
                padding: '8px 16px',
                background: 'transparent',
                border: '1px solid #cbd5e1',
                borderRadius: '8px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                fontSize: '1rem',
                color: '#475569'
            }}
          >
              ← Volver a Categorías
          </button>
          <div>
              <h1 style={{ margin: 0 }}>{selectedCategory.nombre}</h1>
              <p style={{ margin: 0, color: '#64748b' }}>Explorando productos</p>
          </div>
      </div>

      {/* FILTROS AVANZADOS (Compact Version) */}
      <div style={{ 
        marginBottom: '25px', 
        padding: '20px', 
        background: 'white',
        borderRadius: '15px',
        boxShadow: '0 4px 6px rgba(0,0,0,0.05)',
        border: '1px solid #e2e8f0'
      }}>
        <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
          {/* Búsqueda */}
          <input
              type="text"
              placeholder="Buscar..."
              value={filtros.busqueda}
              onChange={(e) => setFiltros({...filtros, busqueda: e.target.value})}
              style={{ padding: '10px', borderRadius: '8px', border: '1px solid #cbd5e1', flex: 1 }}
           />

          {/* Sección */}
          <select
            value={filtros.seccion}
            onChange={(e) => setFiltros({...filtros, seccion: e.target.value})}
            style={{ padding: '10px', borderRadius: '8px', border: '1px solid #cbd5e1' }}
          >
            <option value="">Todas las Secciones</option>
            {secciones.map(s => (
              <option key={s.id} value={s.id}>{s.nombre}</option>
            ))}
          </select>

          {/* Precio */}
           <input
               type="number"
               placeholder="Min $"
               value={filtros.precioMin}
               onChange={(e) => setFiltros({...filtros, precioMin: e.target.value})}
               style={{ width: '80px', padding: '10px', borderRadius: '8px', border: '1px solid #cbd5e1' }}
           />
           <input
               type="number"
               placeholder="Max $"
               value={filtros.precioMax}
               onChange={(e) => setFiltros({...filtros, precioMax: e.target.value})}
               style={{ width: '80px', padding: '10px', borderRadius: '8px', border: '1px solid #cbd5e1' }}
           />

            <select
             value={filtros.ordenPrecio}
             onChange={(e) => setFiltros({...filtros, ordenPrecio: e.target.value})}
             style={{ padding: '10px', borderRadius: '8px', border: '1px solid #cbd5e1' }}
            >
             <option value="none">Orden</option>
             <option value="asc">Menor precio</option>
             <option value="desc">Mayor precio</option>
            </select>
            
            <button onClick={limpiarFiltros} style={{ padding: '10px', background: '#f1f5f9', border: 'none', borderRadius: '8px', cursor: 'pointer' }}>
                Limpiar
            </button>
        </div>
      </div>

      {/* Productos */}
      <div className="productos">
        {productosFiltrados.length === 0 && (
            <div style={{ textAlign: 'center', padding: '40px', width: '100%', gridColumn: '1/-1', color: '#64748b' }}>
                <h3>No hay productos en esta categoría</h3>
                <p>Intenta ajustar los filtros o vuelve más tarde</p>
            </div>
        )}
        {productosFiltrados.map(p => (
          <div key={p.id} className="producto">
            {p.imagen1 ? (
                <img src={p.imagen1} alt={p.nombre} />
            ) : (
                <div style={{ height: '200px', background: '#e2e8f0', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '2rem' }}>📦</div>
            )}
            <h2>{p.nombre}</h2>
            <p className="tienda">Tienda: {p.tienda_nombre}</p>
            <p className="precio">${Number(p.precio).toLocaleString()}</p>
            <p className={`stock ${p.stock > 0 ? 'disponible' : 'agotado'}`}>
              {p.stock > 0 ? `Stock: ${p.stock}` : 'Agotado'}
            </p>
            <button 
              onClick={() => agregarAlCarrito(p)}
              disabled={p.stock <= 0}
              className={p.stock <= 0 ? 'disabled' : ''}
              style={{ marginTop: 'auto' }}
            >
              {p.stock > 0 ? 'Agregar al carrito' : 'Sin Stock'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Catalogo;