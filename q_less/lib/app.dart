import 'package:flutter/material.dart';
import 'package:q_less/style.dart';
import 'SplashScreen.dart';

class App extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
        home: SplashScreen(),
        theme: ThemeData(
          appBarTheme: AppBarTheme(
            textTheme: TextTheme(title: AppBarTextStyle),
          ),
            textTheme: TextTheme(
              title:TitleTextStyle,
              body1: Body1TextStyle,
            )
      )
    );
  }
}