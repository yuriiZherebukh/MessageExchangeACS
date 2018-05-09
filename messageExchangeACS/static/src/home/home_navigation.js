import React from 'react';
import { Link } from 'react-router-dom';

import {List, ListItem} from 'material-ui/List';
import { logged } from '../utils';
import HelpIcon from 'material-ui/svg-icons/action/help-outline';
import CommunicationMessage from 'material-ui/svg-icons/communication/message';
import ActionEvent from 'material-ui/svg-icons/action/event';
import ActionEventSeat from 'material-ui/svg-icons/action/event-seat';
import ProfileIcon from 'material-ui/svg-icons/social/person';


export default class HomeNavigation extends React.Component {
    constructor(props){
        super(props);
    };

    render() {
        return (
            <List>
                {(logged()) ?
                <div>
                    <ListItem
                        key='profile'
                        className='buttonProfile'
                        primaryText='My profile'
                        leftIcon={<ProfileIcon />}
                        containerElement={<Link to='/profile' />}
                    />
                    <ListItem
                        className='buttonMyTrips'
                        primaryText='Messages'
                        leftIcon={<CommunicationMessage />}
                        containerElement={<Link to='/messages' />}
                    />
                    <ListItem
                        className='buttonMyTrips'
                        primaryText='Meetings'
                        leftIcon={<ActionEvent />}
                        containerElement={<Link to='/meetings' />}
                    />
                    <ListItem
                        className='buttonMyTrips'
                        primaryText='Classrooms'
                        leftIcon={<ActionEventSeat />}
                        containerElement={<Link to='/classrooms' />}
                    />
                </div>
                : false}
            </List>
        );
    }
}
