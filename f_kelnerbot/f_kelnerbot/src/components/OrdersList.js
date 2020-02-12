import React, { Component } from 'react'
import PropTypes from 'prop-types'

export default class OrdersList extends Component {
    static propTypes = {
        prop: PropTypes
    }

    render() {
        return (
            <div
            id="menu"
            className="section"
            style={{ paddingTop: "0px", paddingBottom: "0px;" }} >
            <div
              className="bg-image bg-parallax overlay"
              style={{ backgroundImage: "url(./img/background01.jpg)" }}
            ></div>
            <div className="container">
              <div className="row">
                <div id="menu-content" className="tab-content">
                  <div className="col-md-12">
                    <div className="col-md-6 order-md-6 mb-4">
                     
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )
    }
}
