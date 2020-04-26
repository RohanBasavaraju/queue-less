import 'package:flutter/material.dart';

main(){
  runApp(helper());
}

helper(){
  MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: Text('QLess'),
      ),
    ),
  );
}