import React from "react";
import { useState, useEffect } from "react";

function Order({ items, setCart }) {

  const handleRemoveItem = (id) => {
    const updatedCart = items.filter((item) => item.id !== id);
    setCart(updatedCart);
  };

  const cartHTML = items.map((item, index) => (
    <div className="cart-item" key={index}>
      <p>{`${item.name}: $ ${item.price} x`}</p>
      <button onClick={() => handleRemoveItem(item.id)}>Remove</button>
    </div>
  ));

  return (
    <div>
      {cartHTML}
    </div>
  );
}


export default Order;
