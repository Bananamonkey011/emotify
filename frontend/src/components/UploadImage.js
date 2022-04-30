import React, { useState } from "react";
import Webcam from "react-webcam";

const WebcamComponent = () => <Webcam />;

const videoConstraints = {
    width: 220,
    height: 200,
    facingMode: "user",
};

export const WebcamCapture = () => {
    //State to manage image
    const [image, setImage] = useState("");
    //webcam ref
    const webcamRef = React.useRef(null);

    // Callback function to setImage based on webcam screenshot
    const capture = React.useCallback(() => {
        const imageSrc = webcamRef.current.getScreenshot();
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image: imageSrc })
        };
        fetch( "http://127.0.0.1:5000/model", requestOptions)
        .then(response => response.text())
        .then( data => console.log(data));

        setImage(imageSrc);
    });

    return (
        <div className="webcam-container">
            {/* Boundry Box source take from flask route in backend/app.py */}
            {/* <div className="webcam-img">
                <img style={{ height: "100%", borderRadius: "20px", transform: "scaleX(-1)" }} src={"http://127.0.0.1:5000/video_feed"} />
            </div> */}

            {/* Display live camera feed or most recent capture depinding on if an image has been captured */}
            <div className="webcam-img">
                {image == "" ? (
                    <Webcam
                        style={{ height: "100%", borderRadius: "20px", }}
                        audio={false}
                        mirrored
                        screenshotQuality={0.12}
                        ref={webcamRef}
                        screenshotFormat="image/jpeg"
                        videoConstraints={videoConstraints}
                    />
                ) : (
                    <img
                        style={{ height: "100%", borderRadius: "20px" }}
                        src={image}
                    />
                )}
            </div>
                
                {image != "" && 
                    console.log(image)
                }
            {/* Take Screenshot button switches to retake image if image has been captured already  */}
            <div>
                {image != "" ? (
                    <button
                        onClick={(e) => {
                            e.preventDefault();
                            setImage("");
                        }}
                        className="webcam-btn"
                    >
                        Retake Image
                    </button>
                ) : (
                    <button
                        onClick={(e) => {
                            e.preventDefault();
                            capture();
                        }}
                        className="webcam-btn"
                    >
                        Capture
                    </button>
                )}
            </div>
        </div>
    );
};

export default WebcamCapture;
