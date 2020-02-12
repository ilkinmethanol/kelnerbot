import React, { Component } from 'react'
import axios from 'axios';
import SingleTabMenu from './SingleTabMenu';
import Orders from './Orders';
import OrdersList from './OrdersList';
export class Meals extends Component {
state = {
  menu_list : [],
  order_list : [],
}
  componentDidMount(){
    console.log("component mounted");
    
    axios.get('http://localhost:8000/a_rest/restaurant/menulist/').then(
      res => {
        const menu_list = res.data;
        this.setState({ menu_list });
        // console.log(menu_list);
      }
    )
  }
  
  orders_list = [];
  

  addOrder(order){
    this.orders_list.push(order)
    this.setState({order_list:this.orders_list})
  }
  render() {
        return (
        <div id="menu" className="section">
        <div className="bg-image bg-parallax overlay" style={{ backgroundImage: "url(./img/background01.jpg)" }}></div>
        <div className="container">
          <div className="row">
            <div className="section-header text-center">
              <h4 className="sub-title">Discover</h4>
              <h2 className="title white-text">Our Menu</h2>
            </div>
            <ul className="menu-nav">
              {
                this.state.menu_list.map((menu_item,key)=>{
                  return <li><a data-toggle="tab" href={'#'+menu_item.menu_pid}>{menu_item.name}</a></li>
                })
              }
            </ul>
            <div id="menu-content" className="tab-content">
              {
                this.state.menu_list.map((menu_element,key)=>{
                  // console.log("+++++++++++++++",menu_element.products)
                    return <SingleTabMenu menu_dish_list={menu_element.products} menu_pid={menu_element.menu_pid} addOrder={this.addOrder.bind(this)}></SingleTabMenu>
                })
              }
               
                             
            </div>
          </div>
        </div>

        <Orders orders = {this.state.order_list} order_count={this.state.order_list.length} ></Orders>
        <OrdersList></OrdersList>
      </div>

      
        )
    }
}

export default Meals
