import React from 'react';

import { CardTitle } from 'material-ui/Card';
import Paper from 'material-ui/Paper';
import { Link } from 'react-router-dom';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import { blue500 } from 'material-ui/styles/colors';
import { fieldIsEmpty } from '../utils';

import { postClassroom } from './classroom.service';

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

export default class ClassroomCreate extends React.Component{

    constructor(props){
        super(props);
        this.state={
            open: false,
            number: '',
            size: '',
            numberError: '',
            sizeError:'',
        };
    }

    onChange = (event, Value) => {
        this.setState({[event.target.name]: parseInt(Value)});
    };

    helpPostEvent = (event) => {
        const number = this.state.number;
        const size = this.state.size;
        let numberValidation = fieldIsEmpty(number);
        let sizeValidation = fieldIsEmpty(size);
        if (!numberValidation && !sizeValidation) {
            postClassroom(number, size)
                .then((response) => {
                    window.location.reload();
                })
        } else {
            this.setState({'numberError': numberValidation});
            this.setState({'sizeError': sizeValidation});
        }
        event.preventDefault();
    };

    render(){
        return(
            <div className="helpMessageContainer">
                <CardTitle
                    title='Create a classroom'
                    className='helpTitleMailSender'
                    style={{paddingBottom: 0}}
                />
                <TextField
                    hintText="Number"
                    floatingLabelText="Enter number of classroom"
                    className="helpTextInput"
                    name="number"
                    onChange={this.onChange}
                    errorText={this.state.numberError}
                    style={{marginTop: 0}}
                /><br/>
                <TextField
                    hintText="Size"
                    floatingLabelText="Enter classroom size"
                    multiLine={true}
                    rows={1}
                    rowsMax={6}
                    className="helpTextInput"
                    name="size"
                    onChange={this.onChange}
                    errorText={this.state.sizeError}
                    style={{marginTop: 0}}
                /><br/>
                <RaisedButton
                   label="Create" primary={true}
                   onTouchTap={this.helpPostEvent}
                   style={style.button}
                />
            </div>
        )
    }
}
