// frontend/src/App.js
import React from 'react';
import ListaEntregas from './components/ListaEntregas';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Sistema de Trazabilidad de Entregas</h1>
      </header>
      <main>
        <ListaEntregas />
        {/* Agrega más componentes según sea necesario */}
      </main>
    </div>
  );
}

export default App;
