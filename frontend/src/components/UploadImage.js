import React from "react";
import Webcam from "react-webcam";

const WebcamComponent = () => <Webcam />;

const UploadImage = () => {
  return (
    <div>
      <div className="Webcam">
        <Webcam
          audio={false}
          width={"50%"}
          screenshotFormat="image/png"  
        >

        {({ getScreenshot }) => (
          <button
            onClick={() => {
              const imageSrc = getScreenshot();
            }}
          >
            Capture photo
          </button>
        )}
        </Webcam>

        
      </div>
    </div>
  );
};

export default UploadImage;
