import React, {useState} from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; 


export default function Upload() {
    const [link, setLink] = useState("");
    const [username, setUsername] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const backendUrl = import.meta.env.VITE_BACKEND_URL;

        try{
            console.log(link)
            const response = await axios.post(`${backendUrl}/upload_csv`, {
                username: username,
                csv_url: link,
            }, { headers: {
                'Content-Type': 'application/json'  
            }});

            console.log(response.data);
            
            navigate(`/user/${username}`);

        }
        catch(error){
            console.error('Error:', error);
            alert('Failed to upload CSV');
        }
        
    }
   
    const  handleChangeUser = (e) => {
        setUsername(e.target.value)
        
    }
    const handleChangeCsv = (e) => {
        setLink(e.target.value)
        
    }
  return (
    <div>
    <form onSubmit={handleSubmit}>
        <div>
            <label className='block mb-4'>Provide the link to CSV file</label>
            <input onChange={handleChangeUser} value={username} required className='w-full px-4 py-2 mb-4 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500'type = "text" placeholder='username'></input>
            <input onChange={handleChangeCsv} value={link} required className='w-full px-4 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500'type = "text" placeholder='Public link'></input>
            <button className= 'mt-4'type="submit" style={{ padding: '10px 20px' }}>Submit</button>
        </div>
    </form>
    </div>
  )
}
