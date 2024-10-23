import React from 'react';

const truncateText = (text, maxLength) => {
    return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
};

const GameTable = ({ games }) => {
    return (
      <div style={{width: "1200px", maxHeight: "600px", overflow: "auto"}}className="container mt-4">
        <table className="table custom-table table-hover table-bordered table-striped">
          <thead className="thead-dark">
            <tr>
              <th>App ID</th>
              <th>Name</th>
              <th>Release Date</th>
              <th>Required Age</th>
              <th>Price ($)</th>
              <th>DLC Count</th>
              <th>About the Game</th>
              <th>Supported Languages</th>
              <th>Windows</th>
              <th>Mac</th>
              <th>Linux</th>
              <th>Positive Reviews</th>
              <th>Negative Reviews</th>
              <th>Score Rank</th>
              <th>Developers</th>
              <th>Publishers</th>
              <th>Categories</th>
              <th>Genres</th>
              <th>Tags</th>
            </tr>
          </thead>
          <tbody>
            {games.map((game) => (
              <tr key={game.app_id}>
                <td>{game.app_id}</td>
                <td>{game.name}</td>
                <td>{game.release_date}</td>
                <td>{game.required_age}</td>
                <td>{game.price}</td>
                <td>{game.dlc_count}</td>
                <td>{truncateText(game.about_game, 100)}</td>
                <td>{game.supported_languages}</td>
                <td>{game.windows ? 'Yes' : 'No'}</td>
                <td>{game.mac ? 'Yes' : 'No'}</td>
                <td>{game.linux ? 'Yes' : 'No'}</td>
                <td>{game.positive_reviews}</td>
                <td>{game.negative_reviews}</td>
                <td>{game.score_rank}</td>
                <td>{game.developers}</td>
                <td>{game.publishers}</td>
                <td>{game.categories}</td>
                <td>{game.genres}</td>
                <td>{game.tags}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  
  export default GameTable;