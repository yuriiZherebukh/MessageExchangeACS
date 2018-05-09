import React from 'react';

import Paper from 'material-ui/Paper';
import ListItem from 'material-ui/List/ListItem';
import moment from 'moment';

import { getMessages } from './message.service';

const styles = {
    paperStyle : {
        margin:"5% auto",
        padding: "20px",
        width:"90%",
    },
    PaperZDepth : 2,
    header: {
      color: "red",
    },
    time: {
      float: "right",
    },
    messageTime: {
      display: "block"
    },
};

export default class Messages extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            messages: [],
        };
    }

    renderData = () => {
        getMessages()
            .then(response => {
                this.setState({messages: [...response.data]});
            });
    }
    componentDidMount() {
        this.renderData();
    };

    parseDate = (date) =>{
        let day=new Date(date.replace(' ','T')+'Z');
        return day.toUTCString()
    }

    renderMessages () {
        return this.state.messages.map((message, index) => (
                <div key={index}>
                    <Paper style={styles.paperStyle} zDepth={styles.PaperZDepth} >
                    <span style={styles.header}>From: </span><span>{message.user.email}</span>
                    <br/>
                    <span style={styles.header}>Header: </span><span >{message.header}</span>
                    <div style={styles.time}>{this.parseDate(message.created_at)}</div>
                    <br/><br/>
                    <div >{message.body}</div>

                    </Paper>
                </div>

            )
          )
        };

    render() {
      if(this.state.messages.length == 0){
        return <div><h2>No messages yet</h2></div>
      } else{
            return <div>{this.renderMessages()}</div>
      };
    }
  }
