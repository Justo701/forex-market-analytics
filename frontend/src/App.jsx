import { useEffect, useState } from "react"

function App() {
  const [prices, setPrices] = useState([])

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/api/prices`)
      .then(response => response.json())
      .then(data => setPrices(data))
  }, [])

  return (
    <div>
      <h1>Forex Market Analytics</h1>

      <h2>Latest Prices</h2>

      {prices.map((price, index) => (
        <p key={index}>
          {price.pair}: {price.close_price}
        </p>
      ))}
    </div>
  )
}

export default App
