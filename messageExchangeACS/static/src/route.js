import React from "react";
import { Route, Switch } from 'react-router-dom';

import Home from "./home/home";
import Login from "./registration/login";
import Registration from "./registration/registration";
import Profile from "./profile/profile";
import ProfileByID from "./profile/profileByID";
import Message from "./message/message";
import MessagesMain from "./message/messages_main";
import ClassroomsMain from "./classroom/classrooms_main";
import ClassroomCreateMain from "./classroom/classroomCreateMain";
import MeetingsMain from "./meeting/meetingsMain";
import MeetingCreateMain from "./meeting/meetingCreateMain";
import NotFound from './notFound';


export default class MainRoute extends React.Component {
    componentDidMount = () => {
        if (window.location.hash == '#_=_') {
            window.location.hash = '';
            history.pushState('', document.title, window.location.pathname);
        }
    }
    render() {
        return (
            <main>
                <Switch>
                    <Route exact path='/' component={Home} />
                    <Route exact path='/registration'
                        render={(props) => <Registration
                            loginHandler={this.props.loginHandler}
                            {...props}
                        /> }
                    />
                    <Route exact path='/login/:hash?'
                        render={(props) => <Login
                            loginHandler={this.props.loginHandler}
                            {...props}
                        />}
                    />
                    <Route exact path="/profile/" component={Profile} />
                    <Route exact path="/profile/:id" component={ProfileByID} />
                    <Route exact path="/message/" render={(props) => <Message
                            loginHandler={this.props.loginHandler}
                            {...props}
                        /> }
                    />
                    <Route exact path="/messages/" component={MessagesMain} />
                    <Route exact path="/classrooms/" component={ClassroomsMain} />
                    <Route exact path="/classroom/" render={(props) => <ClassroomCreateMain
                            loginHandler={this.props.loginHandler}
                            {...props}
                        /> }
                    />
                    <Route exact path="/meetings/" component={MeetingsMain} />
                    <Route exact path="/meeting/" component={MeetingCreateMain} />
                    <Route component={NotFound} />
                </Switch>
            </main>
        );
    }
}
