This folder catches the intermediate files generated by the build process.
In our hosted application, the server shuts down automatically and this folder is destroyed and emptied if the client has no action for 10 minutes.
Each new invocation of the server will create an empty folder "sent_data".