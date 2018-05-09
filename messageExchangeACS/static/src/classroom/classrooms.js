import React from 'react';

import Paper from 'material-ui/Paper';
import { Link } from 'react-router-dom';
import RaisedButton from 'material-ui/RaisedButton';

import moment from 'moment';

import { getClassrooms, getClassroom  } from './classroom.service';

const styles = {
    paperStyle : {
        margin:"5% auto",
        padding: "20px",
        width:"60%",
    },
    PaperZDepth : 2,
    header: {
      color: "red",
    },
    image: {
        width: "300px",
        height: "300px",
    },
    myTrips : {
        align: "center",
    },
};

export default class Classrooms extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            classrooms: [],
        };
    }

    renderData = () => {
        getClassrooms()
            .then(response => {
                this.setState({classrooms: [...response.data]});
            });
    }
    componentDidMount() {
        this.renderData();
    };

    renderClassrooms () {
        return this.state.classrooms.map((classroom, index) => (
                <div key={index}>
                    <Paper style={styles.paperStyle} zDepth={styles.PaperZDepth} >
                    <img src="/static/src/img/1_page.jpg" style={styles.image}/>
                    <div>
                        <span style={styles.header}>Size: </span><span>{classroom.size}</span>
                        <br/>
                        <span style={styles.header}>Number: </span><span >{classroom.number}</span>
                    </div>
                    </Paper>
                </div>
            )
          )
        };

    render() {
      if(this.state.classrooms.length == 0){
        return <div>
                <RaisedButton
                label='CREATE A CLASSROOM'
                secondary={true}
                labelStyle = { styles.myTrips }
                containerElement={<Link to="/classroom"/>}
                />
                <div><h2>No classrooms yet</h2></div>
              </div>
      } else{
            return <div>
                <RaisedButton
                label='CREATE A CLASSROOM'
                secondary={true}
                labelStyle = { styles.myTrips }
                containerElement={<Link to="/classroom"/>}
                />
                {this.renderClassrooms()}
            </div>
      };
    }
  }
