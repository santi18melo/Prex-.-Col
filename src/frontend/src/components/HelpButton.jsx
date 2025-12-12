import React, { useState } from 'react';
import './HelpButton.css';

const HelpButton = () => {
  const [showModal, setShowModal] = useState(false);

  const openManual = () => {
    // Abrir el manual en una nueva pestaña
    window.open('http://localhost:8000/api/docs/MANUAL_USUARIO_COMPLETO.html', '_blank');
  };

  const toggleModal = () => {
    setShowModal(!showModal);
  };

  return (
    <>
      {/* Botón flotante */}
      <div className="help-button-container">
        <button 
          className="help-button" 
          onClick={toggleModal}
          title="Ayuda y Soporte"
          aria-label="Ayuda"
        >
          <span className="help-icon">🆘</span>
        </button>
      </div>

      {/* Modal de ayuda rápida */}
      {showModal && (
        <div className="help-modal-overlay" onClick={toggleModal}>
          <div className="help-modal" onClick={(e) => e.stopPropagation()}>
            <div className="help-modal-header">
              <h3>🆘 Centro de Ayuda</h3>
              <button className="close-btn" onClick={toggleModal}>✕</button>
            </div>
            
            <div className="help-modal-content">
              <div className="help-section">
                <h4>📖 Documentación</h4>
                <button className="help-link-btn" onClick={openManual}>
                  📚 Manual de Usuario Completo
                </button>
                <button className="help-link-btn" onClick={() => window.open('http://localhost:8000/api/docs/', '_blank')}>
                  📄 Documentación Técnica
                </button>
              </div>

              <div className="help-section">
                <h4>🎯 Accesos Rápidos</h4>
                <div className="quick-links">
                  <a href="#/catalogo">🛒 Ver Catálogo</a>
                  <a href="#/mis-pedidos">📦 Mis Pedidos</a>
                  <a href="#/perfil">👤 Mi Perfil</a>
                </div>
              </div>

              <div className="help-section">
                <h4>📞 Soporte</h4>
                <div className="support-info">
                  <p>📧 <strong>Email:</strong> soporte@prexcol.com</p>
                  <p>📞 <strong>Teléfono:</strong> +57 300 123 4567</p>
                  <p>🕐 <strong>Horario:</strong> Lun-Vie 8AM-6PM</p>
                </div>
              </div>

              <div className="help-section">
                <h4>⌨️ Atajos de Teclado</h4>
                <div className="keyboard-shortcuts">
                  <div className="shortcut">
                    <kbd>Ctrl</kbd> + <kbd>K</kbd>
                    <span>Búsqueda rápida</span>
                  </div>
                  <div className="shortcut">
                    <kbd>Ctrl</kbd> + <kbd>H</kbd>
                    <span>Abrir ayuda</span>
                  </div>
                  <div className="shortcut">
                    <kbd>F1</kbd>
                    <span>Manual completo</span>
                  </div>
                  <div className="shortcut">
                    <kbd>Esc</kbd>
                    <span>Cerrar modal</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="help-modal-footer">
              <p className="version-info">PREXCOL v2.0 - Diciembre 2025</p>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default HelpButton;
