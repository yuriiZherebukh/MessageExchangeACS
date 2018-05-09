import React from "react";

import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import {withRouter} from 'react-router';


import {loginService, registerService} from './registration.service';
import { emailIsNotValid, EMAIL_REGEXP, fieldIsEmpty } from './../utils';

import './registration.less'

const style = {
    paperStyle : {
        margin:"5% auto",
        width:"40%",
    },

    PaperZDepth : 2,

    RaisedButtonStyle : {
        margin:"5%"
    },

    LabelSize : {
        fontSize:"1.2em"
    }

}

export default class Registration extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            first_name:'',
            last_name:'',
            email:'',
            password:'',
            confirmPassword:'',
            passwordError:'',
            emailError:'',
            confirmPasswordError: '',
            serverError:''
        };
    }

    handleEmail = event => {
        this.setState({'email': event.target.value});
    }

    handlePassword = event => {
        this.setState({'password': event.target.value});
    }

    handleConfirmPassword = event => {
        this.setState({'confirmPassword': event.target.value});
    }

    handleFirstName = event => {
        this.setState({'first_name': event.target.value});
    }

    handleLastName = event => {
        this.setState({'last_name': event.target.value});
    }

    handleSubmit = event => {
        const email = this.state.email;
        const first_name = this.state.first_name;
        const last_name = this.state.last_name;
        const password = this.state.password;
        const confirmPassword = this.state.confirmPassword;
        let emailValidation = emailIsNotValid(email);
        let passwordValidation = fieldIsEmpty(password);
        let confirmPasswordValidation = password == confirmPassword;
        if ( !emailValidation && !passwordValidation && confirmPasswordValidation) {
            registerService(email, password, confirmPassword, first_name, last_name)
                .then(() => {
                        this.props.history.push('/login');
                })
                .catch( (error) => {
                    const consoleErrorLog = error.response.data;
                    if (consoleErrorLog.hasOwnProperty("email")){
                        this.setState({"serverError":consoleErrorLog.email[0]});
                    }else{
                    this.setState({"serverError":consoleErrorLog});
                    }
                })
        } else {
            this.setState({'emailError': emailValidation});
            this.setState({'passwordError': passwordValidation});
            this.setState({'confirmPasswordError': "Passwords are not matched"});
        }
        event.preventDefault();
    }

    render() {
        return (
            <Paper style = {style.paperStyle} zDepth={style.PaperZDepth} >
                <div className='form_fields'>
                    <h1>REGISTRATION</h1>
                    <TextField
                        onChange={this.handleFirstName}
                        hintText="Name"
                        name="first_name"
                    />
                    <TextField
                        onChange={this.handleLastName}
                        hintText="Surname"
                        name="last_name"
                    />
                    <TextField
                        onChange={this.handleEmail}
                        hintText="Email"
                        errorText={this.state.emailError}
                        name="email"
                        type="text"
                    />
                    <TextField
                        onChange={this.handlePassword}
                        hintText="Password"
                        errorText={this.state.passwordError}
                        name="password"
                        type='password'
                    />
                     <TextField
                        onChange={this.handleConfirmPassword}
                        hintText="Confirm Password"
                        errorText={this.state.confirmPasswordError}
                        name="confirmPassword"
                        type='password'
                    />
                    <RaisedButton label="Sign UP"
                        primary={true}
                        onTouchTap={this.handleSubmit}
                        style={ style.RaisedButtonStyle }
                        labelStyle = { style.LabelSize }
                     />
                     <p className='serverError'>{this.state.serverError}</p>
                </div>
            </Paper>
        );
    }
}

