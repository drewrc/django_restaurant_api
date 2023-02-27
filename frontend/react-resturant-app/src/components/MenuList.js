import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "./MenuList.css";
import { useState, useEffect } from "react";
import Order from "./Order.js";
import MenuItem from "./MenuItem.js";
import { nanoid } from "nanoid";
import Cookies from "js-cookie";

function MenuList(props) {
  const { setCart } = props;
  const [carts, setCarts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [items, setItems] = useState([]);
  const [user, setUser] = useState("");

  const [subTotal, setSubTotal] = useState(0);

  useEffect(() => {
    // Calculate the subtotal of all items in the cart whenever the items prop changes
    const newSubTotal = carts.reduce((acc, item) => acc + parseFloat(item.price), 0);
    setSubTotal(newSubTotal);
  }, [carts]);

  const handleSubmit = async (event) => {
    alert('you clicked')
    event.preventDefault();
    const orderData = {
      user: user,
      items: carts.map((item) => item.id),
      order_total: carts.reduce((acc, item) => acc + parseFloat(item.price), 0),
    };
    console.log("Submitting order:", orderData);
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
      },
      body: JSON.stringify(orderData),
    };

    const response = await fetch("/api_v1/orders/", options);
    if (!response.ok) {
      console.log(response.status);
      throw new Error("Network response was not OK");
    }
    const data = await response.json();
    setCarts([]);
    // setSubTotal(0);
    setUser("");
    alert("Your order has been submitted!");
    
  };

  useEffect(() => {
    const getItems = async () => {
      const response = await fetch(`/api_v1/items/`);
      if (!response.ok) {
        throw new Error("Network response was not OK");
      }
      const data = await response.json();
      setItems(data);
    };
    getItems();
  }, []);

  const handleRemoveItem = (id) => {
    const updatedCart = carts.filter((item) => item.id !== id);
    setCarts(updatedCart);
  };

  const addToCart = (item) => {
    setCarts([...carts, item]);
  };


  const filteredMenu = items.filter((item) => item.category === selectedCategory)
    .map((item) => (
      <MenuItem 
        key={item.id} 
        {...item} 
        addToCart={addToCart} 
        handleRemoveItem={() => handleRemoveItem(item.id)}
      />
      ))

  return (
    <div>
      <Container>
  
      <Row>
      <Col md={2}>
        <div className="main-menu">
          <div className="side-options">
                <button onClick={() => setSelectedCategory("appetizer")}>Appetizers</button>
                <button onClick={() => setSelectedCategory("entree")}>Entrees</button>
                <button onClick={() => setSelectedCategory("dessert")}>Desserts</button>
                <button onClick={() => setSelectedCategory("side")}>Sides</button>
                <button onClick={() => setSelectedCategory("drink")}>Drinks</button>
            </div>
            </div>
        </Col>
        <Col md={10}>
            <section className="selected-menu-container">
              Menu Items:
              {filteredMenu}
            </section>
          </Col>

        </Row>


        <Row> 
          <div>
          <h2>Your cart:</h2>
          {/* {cartHTML} */}
          </div>

          <Col className="cart-options" md={6}>
      
            <div className="cart-container">
              <h2>Order Summary</h2>
              Order Total: ${subTotal.toFixed(2)}
            </div>
          </Col>

          <Col>
            <div>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="user">Name</label>
                <input type="text" className="form-control" value={user} onChange={(event) => setUser(event.target.value)} placeholder="Enter Name" />
              </div>
              <button type="submit" className="btn btn-primary">Submit</button>
              </form>
              </div>
              <form onSubmit={handleSubmit}>
              <Order items={carts} setCart={setCarts} />
              </form>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
export default MenuList;