import React, { useState } from 'react';
import Webcam from "react-webcam";


const WebcamComponent = () => <Webcam />;

const videoConstraints = {
    width: 220,
    height: 200,
    facingMode: "user"
};

export const WebcamCapture = () => {

    //State to manage image
    const [image,setImage]=useState('');
    //webcam ref
    const webcamRef = React.useRef(null);

    // Callback function to setImage based on webcam screenshot
    const capture = React.useCallback(
        () => {
        const imageSrc = webcamRef.current.getScreenshot();
        setImage(imageSrc)
        });


    return (
        <div className="webcam-container">
            {/* Display live camera feed or most recent capture depinding on if an image has been captured */}
            <div className="webcam-img">
                {image == '' ? <Webcam style={{height: "100%", borderRadius: "20px"}}
                    audio={false}
                    mirrored
                    ref={webcamRef}
                    screenshotFormat="image/jpeg"
                    videoConstraints={videoConstraints}
                /> : <img style={{height: "100%", borderRadius: "20px"}} src={image} />}
            </div>

            {/* Take Screenshot button switches to retake image if image has been captured already */}
            <div>
                {image != '' ?
                    <button onClick={(e) => {
                        e.preventDefault();
                        setImage('')
                    }}
                        className="webcam-btn">
                        Retake Image</button> :
                    <button onClick={(e) => {
                        e.preventDefault();
                        capture();
                    }}
                        className="webcam-btn">Capture</button>
                }
                {/* Overlay div box to show results of face detection algorithm */}
                {/* <div className='faceOverlay'/> */}
            </div>
        </div>
    );
};


export default WebcamCapture;
