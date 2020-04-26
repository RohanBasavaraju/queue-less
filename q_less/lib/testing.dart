import 'package:flutter/material.dart';

main(){
  runApp(splashScreen());
}

splashScreen(){
  return MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: Text('QLess'),
      ),
      body: Text('Welcome to QLess!')
    ),
  );
}