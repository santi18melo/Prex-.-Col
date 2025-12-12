import React, { useState } from 'react';
import ModalEdicion from '../../ModalEdicion';

export default function AdminCategoriesTab({ categorias, loading, onCreate, onUpdate, onDelete }) {
  const [showModal, setShowModal] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState(null);

  const handleEdit = (category) => {
    setSelectedCategory(category);
    setShowModal(true);
  };

  const handleCreate = () => {
    setSelectedCategory({});
    setShowModal(true);
  };

  const handleDelete = (id) => {
    if (window.confirm('¿Estás seguro de eliminar esta categoría?')) {
      onDelete(id);
    }
  };

  const handleSubmit = async (formData) => {
    try {
        if (selectedCategory && selectedCategory.id) {
            await onUpdate({ ...formData, id: selectedCategory.id });
        } else {
            await onCreate(formData);
        }
        setShowModal(false);
        setSelectedCategory(null);
    } catch (error) {
        console.error("Error saving category:", error);
        alert("Error al guardar categoría");
    }
  };

  if (loading) return <div className="loading-spinner">Cargando categorías...</div>;

  return (
    <div className="content-section">
      <div className="section-header">
        <h2>Gestión de Categorías</h2>
        <button className="btn-primary" onClick={handleCreate}>
          + Nueva Categoría
        </button>
      </div>

      <div className="table-responsive">
        <table className="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Imagen</th>
              <th>Nombre</th>
              <th>Descripción</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {(categorias || []).map((cat) => (
              <tr key={cat.id}>
                <td>#{cat.id}</td>
                <td>
                  {cat.imagen ? (
                    <img 
                      src={cat.imagen} 
                      alt={cat.nombre} 
                      style={{ width: '40px', height: '40px', objectFit: 'cover', borderRadius: '4px' }} 
                    />
                  ) : (
                    <div style={{ width: '40px', height: '40px', background: '#eee', borderRadius: '4px' }}></div>
                  )}
                </td>
                <td><strong>{cat.nombre}</strong></td>
                <td>{cat.descripcion || '-'}</td>
                <td>
                  <span className={`badge ${cat.activa ? 'badge-active' : 'badge-inactive'}`}>
                    {cat.activa ? 'Activa' : 'Inactiva'}
                  </span>
                </td>
                <td>
                  <div className="actions-cell">
                    <button className="btn-icon edit" onClick={() => handleEdit(cat)} title="Editar">✏️</button>
                    <button className="btn-icon delete" onClick={() => handleDelete(cat.id)} title="Eliminar">🗑️</button>
                  </div>
                </td>
              </tr>
            ))}
            {(!categorias || categorias.length === 0) && (
                <tr>
                    <td colSpan="6" style={{textAlign: 'center', padding: '20px'}}>No hay categorías registradas</td>
                </tr>
            )}
          </tbody>
        </table>
      </div>

      <ModalEdicion
        visible={showModal}
        tipo="Categoria"
        datos={selectedCategory}
        onClose={() => setShowModal(false)}
        onSubmit={handleSubmit}
      />
    </div>
  );
}
