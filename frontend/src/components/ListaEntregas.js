// frontend/src/components/ListaEntregas.js
import React, { useState, useEffect } from 'react';

const ListaEntregas = () => {
    const [entregas, setEntregas] = useState([]);

    useEffect(() => {
        // Solicitud HTTP
        // URL
        fetch('http://localhost:5000/pedidos')
            .then(response => response.json())
            .then(data => setEntregas(data));
    }, []);

    return (
        <div>
            <h2>Lista de Entregas</h2>
            <ul>
                {entregas.map(entrega => (
                    <li key={entrega.id}>
                        {`ID: ${entrega.id}, Fecha de Llegada: ${entrega.fecha_llegada}`}
                        {}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ListaEntregas;
