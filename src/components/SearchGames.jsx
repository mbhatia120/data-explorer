import React, { useState } from 'react';
import axios from 'axios';
import GameTable from './GameTable';


const SearchGames = ({username}) => {
  
  const [searchParams, setSearchParams] = useState({
    username: `${username}`,
    app_id: '',
    name: '',
    name_condition: 'contains',
    release_date: '',
    release_date_condition: '=',
    required_age: '',
    age_condition: '=',
    price: '',
    price_condition: '=',
    dlc_count: '',
    about_game: '',
    about_game_condition: 'contains',
    supported_languages: '',
    windows: '',
    mac: '',
    linux: '',
    positive: '',
    positive_condition: '=',
    negative: '',
    negative_condition: '=',
    score_rank: '',
    score_rank_condition: '=',
    developer: '',
    publisher: '',
    categories: '',
    genres: '',
    tags: ''
  });

 
  const [results, setResults] = useState([]);

  
  const formFields = [
    // [{ label: 'Username', name: 'username', type: 'text' }],
    [{ label: 'App ID', name: 'app_id', type: 'number' }],
    [{ label: 'Name', name: 'name', type: 'text' }, { label: 'Name Condition', name: 'name_condition', type: 'select', options: ['contains', '='] }],
    [{ label: 'Release Date', name: 'release_date', type: 'text', placeholder: 'e.g. Oct 21, 2008' }, { label: 'Release Date Condition', name: 'release_date_condition', type: 'select', options: ['=', '>', '<'] }],
    [{ label: 'Required Age', name: 'required_age', type: 'number' }, { label: 'Age Condition', name: 'age_condition', type: 'select', options: ['=', '>', '<'] }],
    [{ label: 'Price', name: 'price', type: 'number', step: '0.01' }, { label: 'Price Condition', name: 'price_condition', type: 'select', options: ['=', '>', '<'] }],
    [{ label: 'DLC Count', name: 'dlc_count', type: 'number' }],
    [{ label: 'About the Game', name: 'about_game', type: 'text' }, { label: 'About Game Condition', name: 'about_game_condition', type: 'select', options: ['contains', '='] }],
    [{ label: 'Supported Languages', name: 'supported_languages', type: 'text' }],
    [{ label: 'Windows Support', name: 'windows', type: 'select', options: ['', 'true', 'false'] }],
    [{ label: 'Mac Support', name: 'mac', type: 'select', options: ['', 'true', 'false'] }],
    [{ label: 'Linux Support', name: 'linux', type: 'select', options: ['', 'true', 'false'] }],
    [{ label: 'Positive Reviews', name: 'positive', type: 'number' }, { label: 'Positive Condition', name: 'positive_condition', type: 'select', options: ['=', '>', '<'] }],
    [{ label: 'Negative Reviews', name: 'negative', type: 'number' }, { label: 'Negative Condition', name: 'negative_condition', type: 'select', options: ['=', '>', '<'] }],
    [{ label: 'Score Rank', name: 'score_rank', type: 'number', step: '0.1' }, { label: 'Score Rank Condition', name: 'score_rank_condition', type: 'select', options: ['=', '>', '<'] }],
    [{ label: 'Developer', name: 'developer', type: 'text' }],
    [{ label: 'Publisher', name: 'publisher', type: 'text' }],
    [{ label: 'Categories', name: 'categories', type: 'text' }],
    [{ label: 'Genres', name: 'genres', type: 'text' }],
    [{ label: 'Tags', name: 'tags', type: 'text' }],
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setSearchParams({
      ...searchParams,
      [name]: value,
    });
  };

  
  const handleSubmit = async (e) => {
    e.preventDefault();

    
    const filteredSearchParams = Object.fromEntries(
      Object.entries(searchParams).filter(([key, value]) => value !== "")
    );
    const backendUrl = import.meta.env.VITE_BACKEND_URL;
    try {
      const response = await axios.post(`${backendUrl}/api/searchGames`, filteredSearchParams);
      console.log(response.data.games);
      setResults(response.data.games);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="container" style={{width: "1200px"}}>
      <h1 className="text-center my-4">Search Games</h1>
      <form onSubmit={handleSubmit}>
        
        {formFields.map((fieldGroup, groupIndex) => (
          <div key={groupIndex} className="form-group row mb-3">
            {fieldGroup.map((field) => (
              <div key={field.name} className="col-md-6">
                <label className="row d-flex align-items-center form-label">
                  {field.label}:
                  {field.type === 'select' ? (
                    <select className="w-full px-4 py-2 ml-4 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500 form-control" name={field.name} value={searchParams[field.name]} onChange={handleChange}>
                      {field.options.map((option) => (
                        <option key={option} value={option}>
                          {option || 'Any'}
                        </option>
                      ))}
                    </select>
                  ) : (
                    <input
                      className="form-control w-full px-4 py-2 ml-4 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
                      type={field.type}
                      name={field.name}
                      value={searchParams[field.name]}
                      onChange={handleChange}
                      placeholder={field.placeholder || ''}
                      step={field.step || ''}
                    />
                  )}
                </label>
              </div>
            ))}
          </div>
        ))}

       
        <button type="submit" className="btn btn-primary btn-block">Search</button>
      </form>

      
      <div className="results-container mt-4">
        <h2>Results</h2>
        {results.length > 0 ? (
            <GameTable games={results}/>
        ) : (
          <p>No results found</p>
        )}
      </div>
    </div>
  );
};

export default SearchGames;
