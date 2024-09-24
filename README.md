# VideoStreamer

A cross-platform application for sending and receiving video streams between two devices. The sender device captures video and transmits it to the receiver, which decodes and displays the video.

How it works:

   1- Connect your webcam to the sender device(server).

   2- Run the sender code using the following command: "python sender.py" in sender device.

   3- Open receiver.py and replace 0.0.0.0 with the sender ip (you can find it using "ipconfig" in windows or "ifconfig" in linux) in "socket.connect("tcp://0.0.0.0:5555")".

   4- Run receiver.py using the following command: "python sender.py" in receiver device.
