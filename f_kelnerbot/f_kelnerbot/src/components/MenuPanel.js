import React, { Component } from 'react'

export default class App extends Component {
  render() {
    return (
      <header id="header">
      <div id="top-nav">
        <div className="container">
        <div className="logo">
          <a href="index.html">BuffetOverflowRestaurant</a>

        </div>
        <button className="navbar-toggle">
          <span></span>
        </button>
        <ul className="social-nav">
          <li><a href="#"><i className="fa fa-facebook"></i></a></li>
          <li><a href="#"><i className="fa fa-twitter"></i></a></li>
          <li><a href="#"><i className="fa fa-google-plus"></i></a></li>
        </ul>
       
        </div>
      </div>
      <div id="bottom-nav">
        <div className="container">
        <nav id="nav">
          <ul className="main-nav nav navbar-nav">
            <li><a href="index.html">Home</a></li>
            <li><a href="index.html#about">About</a></li>
            <li><a href="index.html#menu">Menu</a></li>
            {/* <li><a href="index.html#reservation">Reservation</a></li> */}
            <li><a href="index.html#events">Events</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
          <ul className="cta-nav">
            {/* <li><a href="index.html#reservation" className="main-button">Reserve</a></li> */}
          </ul>
          <ul className="contact-nav nav navbar-nav">
            <li><a href="tel:0455481497"><i className="fa fa-phone"></i> 640-69-72</a></li>
            <li><a href="#"><i className="fa fa-map-marker"></i> V.Mirzeyev 99/55</a></li>
          </ul>
        </nav>
        </div>
      </div>
    </header>
    )
  }
}
