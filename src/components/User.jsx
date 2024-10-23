import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import GameTable from './GameTable';
import SearchGames from './SearchGames';

export default function User() {
    const { username } = useParams(); 
    const [userData, setUserData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        
        const fetchUserData = async () => {
            try {
                const backendUrl = import.meta.env.VITE_BACKEND_URL;
                const response = await fetch(`${backendUrl}/${username}`);
                if (!response.ok) {
                    throw new Error('User not found');
                }
                const data = await response.json();
                console.log(data);
                setUserData(data);
            } catch (err) {
                setError(err.message);
            }
        };

        fetchUserData();
    }, [username]);

    if (error) {
        return <div>Error: {error}</div>;
    }
    return (
        <div>
            <h1>User Profile - {`${username}`}</h1>
            {userData ? (
                <div>
                    <GameTable games= {userData.games}/>
                    <SearchGames username={username} />
               </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>

    )
}
