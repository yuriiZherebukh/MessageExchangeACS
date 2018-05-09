import React from "react";

import Paper from 'material-ui/Paper';
import ProfileAvatar from './profileAvatar';
import Avatar from 'material-ui/Avatar';
import { ProfileEdit } from './profileEdit';

import { logged, axiosInstance } from '../utils';

import './profile.less';

const profileURL = '/api/v1/profile/';


export default class Profile extends React.Component {
    constructor(props) {
        super(props);
        this.profileID = this.props.match.params.id || '';
        this.state = {
            profile: '',
        };
    }
    componentDidMount(){
        this.getProfile();
    }

    getProfile = () => {
        axiosInstance.get(profileURL)
        .then(response => {
        const profile = response.data;
        this.setState({profile: profile});
        });
    };

    updateProfile = (data) => {
        this.setState({profile: data});
    }

    render(){
    const data = this.state.profile
    let profileElement;
    if (logged()) {
        profileElement = (
          <Paper className='MainPaper'  zDepth={2} >
            {data && <ProfileAvatar src={this.state.profile.avatar} updateProfile={this.updateProfile} />}
            {data && <ProfileEdit profile={data} getProfile={this.getProfile} />}
          </Paper>
          )
    } else {
        profileElement = this.props.history.push('/login')
    }
        return (
            <div>{profileElement}</div>
        );
  };
}
