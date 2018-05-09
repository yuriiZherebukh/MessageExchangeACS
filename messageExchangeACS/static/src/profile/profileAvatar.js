import React from "react";
import Dropzone from 'react-dropzone';
import axios from 'axios';

import Avatar from 'material-ui/Avatar';
import FlatButton from 'material-ui/FlatButton';
import AvatarIcon from 'material-ui/svg-icons/image/portrait';
import Snackbar from 'material-ui/Snackbar';
import { blue500 } from 'material-ui/styles/colors';
import { profileURL } from './profile.service';

import './profile.less';
import {axiosInstance} from '../utils';

const styles = {
  LabelStyle: {
    color: blue500,
  },
  buttonStyle: {
    margin: 18,
  },
};


export default class ProfileAvatar extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
            open: false
        };
    }


    handleDrop = files => {
        const avatar = new FormData();
        avatar.append("file",files)
        axiosInstance.put(profileURL, {avatar})
        .then(response => {
            const data = response.data;
            this.props.updateProfile(data);
        })
    }

    onDropRejected = () => {
        this.setState({open: true});
    }

    handleRequestClose = () => {
        this.setState({
            open: false,
        });
    };

    render(){
        return(
       	<div className='avatar'>
        <Avatar src={this.props.src} className='avatar' size={200} />
        </div>
        );
    };
}