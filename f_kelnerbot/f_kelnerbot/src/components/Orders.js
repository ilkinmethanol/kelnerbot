import React, { Component } from "react";
import axios from 'axios';
export default class Orders extends Component {
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  today = new Date();
  fulldate =
    this.today.getFullYear()+"-"+(this.today.getMonth()+ 1)+"-" +this.today.getDate()+","+this.today.getHours()+":"+this.today.getMinutes()+":"+this.today.getSeconds();

  state = {};
  order_point = [];

  handleSubmit(event) {
    event.preventDefault();
    this.setState({ finalAmount: event.target["total_amount"].value });
    this.setState({customer_ordered_table_number: event.target["tableNumber"].value});
    this.setState({transactionDate:this.fulldate});
    console.log(this.state.customer_ordered_table_number);
    
    alert("Your order accepted")
  }

  render() {
    return (
      <div
        id="menu"
        className="section"
        style={{ paddingTop: "0px", paddingBottom: "0px;" }}
      >
        <div
          className="bg-image bg-parallax overlay"
          style={{ backgroundImage: "url(./img/background01.jpg)" }}
        ></div>
        <div className="container">
          <div className="row">
            <div id="menu-content" className="tab-content">
              <div className="col-md-12">
                <div className="col-md-6 order-md-6 mb-4">
                  <form onSubmit={this.handleSubmit}>
                    <h4 className="d-flex justify-content-between align-items-center mb-3">
                      <span className="text-muted">Your orders</span>

                      <span className="badge badge-secondary badge-pill">
                        {this.props.order_count}
                      </span>
                    </h4>
                    <input
                      placeholder="Enter your table number"
                      style={{ width: "100%" }}
                      name="tableNumber"
                    ></input>
                    <ul className="list-group mb-3">
                      {this.props.orders.map((meal_id, key) => {
                        return (
                          <li
                            className="list-group-item d-flex justify-content-between lh-condensed"
                            key={key}
                          >
                            <div>
                              <h6 className="my-0">{meal_id.dish_name}</h6>
                            </div>
                            <span className="text-muted">
                              {meal_id.dish_price} AZN : {meal_id.dish_quantity}
                              /{meal_id.dish_measure}
                            </span>
                          </li>
                        );
                      })}

                      <li className="list-group-item d-flex justify-content-between">
                        <span>Total : </span>
                        <strong>
                          {this.props.orders.reduce(function(cnt, o) {
                            return cnt + o.dish_price;
                          }, 0)}
                          AZN
                        </strong>
                      </li>
                    </ul>
                    <input
                      name="total_amount"
                      value={this.props.orders.reduce(function(cnt, o) {
                        return cnt + o.dish_price;
                      }, 0)}
                    ></input>
                    <button>Order now</button>
                  </form>
                </div>

                <div className="col-md-6 order-md-6 mb-4">
                  <h4 className="d-flex justify-content-between align-items-center mb-3">
                    <span className="text-muted">Your cheque</span>
                  </h4>
                  <div>Thanks for ordering in BuffetOverFlow</div>
                  <p>
                    
                    Number of table : {this.state.customer_ordered_table_number} <br></br>
                    Adress of restaurant: Vugar Muradov 75A <br></br>AZ1003,
                    Sabail, Bayil, Baku <br></br>
                    {this.fulldate}
                    <ul>
                      <li>Non-fiscal</li>
                    <li>Transaction data and time : {this.state.transactionDate}</li>
                      <li>Operation id </li>
                    <li>Table number {this.state.customer_ordered_table_number}</li>
                      <li>Paid by (Cash / Card)</li>
                    <li>Amount: {this.state.finalAmount}</li>
                      <li>Transaction accepted</li>
                    </ul>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
