import Button from "react-bootstrap/Button";
import "./MenuItem.css";
import { nanoid } from "nanoid";
import { useState, useEffect } from "react";
import Cookies from "js-cookie";

function MenuItem({ name, id, description, price, addToCart, }) {

  return (
    <div>
      <div key={id}>{name}</div>
      {description}
      <div>
        {price}
        <button onClick={() => addToCart({ id, name, price })}>Add to Cart
          +
        </button>
      </div>
    </div>
  );
}

export default MenuItem;
