import React from 'react';

import Paper from 'material-ui/Paper';
import { Link } from 'react-router-dom';
import RaisedButton from 'material-ui/RaisedButton';

import moment from 'moment';

import { getMeetings  } from './meeting.service';

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
    finishes: {
        color: "red",
        marginLeft: "60px",
    },
};

export default class Meetings extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            meetings: []
        };
    }

    renderData = () => {
        getMeetings()
            .then(response => {
                this.setState({meetings: [...response.data]});
            });
    }
    componentDidMount() {
        this.renderData();
    };

    renderMeetings () {
        return this.state.meetings.map((meeting, index) => (
                <div key={index}>
                    <Paper style={styles.paperStyle} zDepth={styles.PaperZDepth} >
                    <div>
                        <span style={styles.header}>Owner user: </span><span>{meeting.owner_user.email}</span>
                        <br/>
                        <span style={styles.header}>Classroom: </span><span >{meeting.classroom.number}</span>
                        <br/><br/>
                        <span style={styles.header}>Name: </span><span >{meeting.name}</span>
                        <br/><br/>
                        <span style={styles.header}>Description: </span><span >{meeting.description}</span>
                        <br/><br/>
                        <span style={styles.header}>Date: </span><span >{meeting.date_of_action}</span>
                        <br/>
                        <span style={styles.header}>Starts: </span><span >{meeting.starts_at}</span>
                        <span style={styles.finishes}>Finishes: </span><span>{meeting.finishes_at}</span>
                    </div>
                    </Paper>
                </div>
            )
          )
        };

    render() {
      if(this.state.meetings.length == 0){
        return <div>
                <RaisedButton
                label='CREATE A MEETING'
                secondary={true}
                labelStyle = { styles.myTrips }
                containerElement={<Link to="/meeting"/>}
                />
                <div><h2>No meetings</h2></div>
              </div>
      } else{
            return <div>
                <RaisedButton
                label='CREATE A MEETING'
                secondary={true}
                labelStyle = { styles.myTrips }
                containerElement={<Link to="/meeting"/>}
                />
                {this.renderMeetings()}
            </div>
      };
    }
  }
