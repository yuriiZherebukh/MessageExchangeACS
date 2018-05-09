import React from 'react';

import { Card, CardHeader, CardMedia, CardText, CardTitle, CardActions } from 'material-ui/Card';
import Paper from 'material-ui/Paper';
import RaisedButton from 'material-ui/RaisedButton';
import MenuItem from 'material-ui/MenuItem';
import SelectField from 'material-ui/SelectField';
import TextField from 'material-ui/TextField';
import Snackbar from 'material-ui/Snackbar';
import { blue500 } from 'material-ui/styles/colors';
import { browserHistory } from 'react-router'

import { postMessage, getUsers } from './message.service';
import { emailIsNotValid, fieldIsEmpty, arrayIsEmpty } from '../utils';

const style = {
    button:{
        margin: 20,
    }
};

const styles = {
  LabelStyle: {
    color: blue500,
    marginLeft: 40
  },
  buttonStyle: {
    margin: 18,
  },
};

export default class MessageButtons extends React.Component{

    constructor(props){
        super(props);
        this.state={
            open: false,
            users_list:[],
            to_users:[],
            user_email:[],
            header:'',
            body:'',
            emailError: '',
            subjectError:'',
            bodyError:'',
        };
    }

    renderData = () => {
        getUsers()
            .then(response => {
                this.setState({users_list: [...response.data]});
            });
    }
    componentDidMount() {
        this.renderData();
    }

    onChange = (event, Value) => {
        this.setState({[event.target.name]: Value});
    };

    onChangeToUser = (event, Value) => {
        this.setState({to_users:[...this.state.to_users, this.state.users_list[Value].id]});
        this.setState({user_email:[... this.state.user_email, this.state.users_list[Value].email]})
    };

    helpPostEvent = (event) => {
        const to_users = this.state.to_users;
        const header = this.state.header;
        const body = this.state.body;
        let toUsersValidation = arrayIsEmpty(to_users);
        let headerValidation = fieldIsEmpty(header);
        let bodyValidation = fieldIsEmpty(body);
        if (!toUsersValidation && !bodyValidation && !headerValidation) {
            postMessage(header, body, to_users)
                .then((response) => {
                    window.location.reload();
                })
        } else {
            this.setState({'emailError': toUsersValidation});
            this.setState({'subjectError': headerValidation});
            this.setState({'messageError': bodyValidation});
        }
        event.preventDefault();
    };

    render(){
        return(
            <div className="helpMessageContainer">
                <CardTitle
                    title='Send your message'
                    className='helpTitleMailSender'
                    style={{paddingBottom: 0}}
                />
                <SelectField
                floatingLabelText="To user:"
                name='to_users'
                value={this.state.to_users}
                style={{width: "200px"}}
                onChange={this.onChangeToUser}
                floatingLabelStyle={styles.LabelStyle}>
                {this.state.users_list.map((user, id) => (
                  <MenuItem
                    key={id}
                    multiple={true}
                    value={user.id}
                    primaryText={user.email}
                    />
                   ))
                }
                </SelectField>
                <TextField
                    hintText="Users"
                    className="helpTextInput"
                    name="user_email"
                    value={this.state.user_email}
                    fullWidth={true}
                    errorText={this.state.emailError}
                    style={{marginTop: 0}}
                />
                <TextField
                    hintText="Subject"
                    floatingLabelText="Enter your subject"
                    className="helpTextInput"
                    name="header"
                    fullWidth={true}
                    onChange={this.onChange}
                    errorText={this.state.subjectError}
                    style={{marginTop: 0}}
                /><br/>
                <TextField
                    hintText="Message Field"
                    floatingLabelText="Enter your message"
                    multiLine={true}
                    fullWidth={true}
                    rows={1}
                    rowsMax={6}
                    className="helpTextInput"
                    name="body"
                    onChange={this.onChange}
                    errorText={this.state.messageError}
                    style={{marginTop: 0}}
                /><br/>
                <RaisedButton
                   label="Send" primary={true}
                   onTouchTap={this.helpPostEvent}
                   style={style.button}
                />
            </div>
        )
    }
}
