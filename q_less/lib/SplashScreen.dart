import 'package:flutter/material.dart';
import 'package:q_less/sections/BigImage.dart';
import 'sections/TextSection.dart';

class SplashScreen extends StatelessWidget{

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("QLess",
            style: TextStyle(fontSize: 36.0, color: Colors.white,
                fontWeight: FontWeight.bold),),
          centerTitle: true,
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            BigImage("assets/images/market.jpg"),
            TextSection('Welcome to the QLess App', 'We help you find the shortest lines'),
          ],
        )
    );
  }
}