import React, { Component } from 'react'
import PropTypes from 'prop-types'

export default class SingleTabMenu extends Component {
  static propTypes = {
    prop: PropTypes
  }

  render() {
    return (
      <div id={this.props.menu_pid} className="tab-pane fade in active">
        {
          this.props.menu_dish_list.map((dish_list,key)=>{
            return( 
            <div className="col-md-12" style={{border:"1px solid black",marginBottom:"3px"}}>
              <div className="single-dish">
              <div className="single-dish-heading">
                  <h4 className="name">{dish_list.dish_name}</h4>
                <h4 className="price">{dish_list.dish_price+"AZN /"+dish_list.dish_quantity+" "+dish_list.dish_measure}</h4>
            <button class="btn btn-primary" onClick={()=>this.props.addOrder(dish_list)}>Add to orders</button>
              </div>
              <img src={dish_list.dish_image} width="100px" style={{float:"left",marginBottom:"3px"}}></img>

            <p>{dish_list.dish_ingredients}</p>
            </div>
          </div>
         
            )
          })
        }
       
      </div>
      
    )
  }
}
