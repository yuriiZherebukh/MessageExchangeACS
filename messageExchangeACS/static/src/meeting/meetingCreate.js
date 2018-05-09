import React from 'react';

import { CardTitle } from 'material-ui/Card';
import Paper from 'material-ui/Paper';
import { Link } from 'react-router-dom';
import MenuItem from 'material-ui/MenuItem';
import SelectField from 'material-ui/SelectField';
import RaisedButton from 'material-ui/RaisedButton';
import DatePicker from 'material-ui/DatePicker';
import TimePicker from 'material-ui/TimePicker';
import TextField from 'material-ui/TextField';
import { blue500 } from 'material-ui/styles/colors';

import moment from 'moment';

import { postMeeting } from './meeting.service';
import { getUsers } from '../message/message.service';
import { getClassrooms } from '../classroom/classroom.service';
import { fieldIsEmpty } from '../utils';

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

export default class MeetingCreate extends React.Component{

    constructor(props){
        super(props);
        this.state={
            open: false,
            users_list: [],
            classrooms: [],
            user_email: [],
            participated_users:[],
            classroom: '',
            name: '',
            description:'',
            classroom_number: '',
            date_of_action: '',
            starts_at: '',
            finishes_at: '',
            classroomError: '',
            participatedUserError:'',
            nameError:'',
            descriptionError:'',
            dateOfActionError:'',
            startsAtError:'',
            finishesAtError:'',
        };
    }

    renderUsers = () => {
        getUsers()
        .then(response => {
            this.setState({users_list: [...response.data]});
        });

    };

    renderClassrooms = () => {
        getClassrooms()
        .then(response => {
            this.setState({classrooms: [...response.data]});
        });
    };

    componentDidMount() {
        this.renderUsers();
        this.renderClassrooms();
    }

    onChange = (event, Value) => {
        this.setState({[event.target.name]: Value});
    };

    onChangeDate =(event, value) => {
        this.setState({date_of_action:moment(value).format("YYYY-MM-DD")});
    };

    onChangeStartsAt =(event, value) => {
        this.setState({starts_at:moment(value).format("HH:MM")});
    };

    onChangeFinishesAt =(event, value) => {
        this.setState({finishes_at:moment(value).format("HH:MM")});
    };

    onChangeParticipatedUser = (event, Value) => {
        this.setState({participated_users:[...this.state.participated_users, this.state.users_list[Value].id]});
        this.setState({user_email:[... this.state.user_email, this.state.users_list[Value].email]})
    };

    onChangeClassroom = (event, Value) => {
        this.setState({classroom:this.state.classrooms[Value].id});
        this.setState({classroom_number:this.state.classrooms[Value].number})
    };

    helpPostEvent = (event) => {
        const classroom = this.state.classroom;
        const participated_user = this.state.participated_users;
        const description = this.state.description;
        const name = this.state.name;
        const date_of_action = this.state.date_of_action;
        const starts_at = this.state.starts_at;
        const finishes_at = this.state.finishes_at;
        let classroomValidation = fieldIsEmpty(classroom);
        let participatedUsersValidation = fieldIsEmpty(participated_user);
        let nameValidation = fieldIsEmpty(name);
        let descriptionValidation = fieldIsEmpty(description);
        let dateOfActionValidation = fieldIsEmpty(date_of_action);
        let startsAtValidation = fieldIsEmpty(starts_at);
        let finishesAtValidation = fieldIsEmpty(finishes_at);


        if (!classroomValidation && !participatedUsersValidation && !nameValidation && !descriptionValidation &&
            !dateOfActionValidation && !startsAtValidation && !finishesAtValidation) {
            postMeeting(classroom, participated_user, name, description, date_of_action, starts_at, finishes_at)
                .then((response) => {
                    window.location.reload();
                })
        } else {
            this.setState({'classroomError': classroomValidation});
            this.setState({'participatedUserError': participatedUsersValidation});
            this.setState({'nameError': nameValidation});
            this.setState({'descriptionError': descriptionValidation});
            this.setState({'dateOfActionError': dateOfActionValidation});
            this.setState({'startsAtError': startsAtValidation});
            this.setState({'finishesAtError': finishesAtValidation});
        }
        event.preventDefault();
    };

    render(){
        return(
            <div className="helpMessageContainer">
                <CardTitle
                    title='Start a meeting'
                    className='helpTitleMailSender'
                    style={{paddingBottom: 0}}
                />
                <SelectField
                floatingLabelText="Include users in meeting:"
                name='participated_users'
                value={this.state.participated_users}
                errorText={this.state.participatedUserError}
                style={{marginTop: 0}}
                onChange={this.onChangeParticipatedUser}
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
                style={{marginTop: 0}}
                />
                <SelectField
                floatingLabelText="Select a classroom"
                name='classroom'
                value={this.state.classroom}
                errorText={this.state.classroomError}
                style={{marginTop: 0}}
                onChange={this.onChangeClassroom}
                floatingLabelStyle={styles.LabelStyle}>
                {this.state.classrooms.map((classroom, id) => (
                  <MenuItem
                    key={id}
                    multiple={true}
                    value={classroom.id}
                    primaryText={classroom.number}
                    />
                   ))
                }
                </SelectField>
                <TextField
                    hintText="Name"
                    floatingLabelText="Enter meeting name"
                    className="helpTextInput"
                    name="name"
                    value={this.state.name}
                    fullWidth={true}
                    onChange={this.onChange}
                    errorText={this.state.nameError}
                    style={{marginTop: 0}}
                /><br/>
                <TextField
                    hintText="Description"
                    floatingLabelText="Enter description"
                    multiLine={true}
                    fullWidth={true}
                    value={this.state.description}
                    rows={1}
                    rowsMax={6}
                    className="helpTextInput"
                    name="description"
                    onChange={this.onChange}
                    errorText={this.state.descriptionError}
                    style={{marginTop: 0}}
                /><br/>
                <DatePicker hintText="Date of action"
                name="date_of_action"
                onChange={this.onChangeDate}
                errorText={this.state.dateOfActionError}
                style={{marginTop: 0}}
                />
                <TimePicker
                  hintText="Starts at"
                  name="starts_at"
                  minutesStep={5}
                  onChange={this.onChangeStartsAt}
                  errorText={this.state.startsAtError}
                  style={{marginTop: 0}}
                  />
                <TimePicker
                  hintText="Finishes at"
                  name="finishes_at"
                  minutesStep={5}
                  onChange={this.onChangeFinishesAt}
                  errorText={this.state.finishesAtError}
                  style={{marginTop: 0}}
                />
                <RaisedButton
                   label="Create" primary={true}
                   onTouchTap={this.helpPostEvent}
                   style={style.button}
                />
            </div>
        )
    }
}
