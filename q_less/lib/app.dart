import 'package:flutter/material.dart';
import 'SplashScreen.dart';

class App extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
        home: SplashScreen(),
        theme: ThemeData(
          appBarTheme: AppBarTheme(
          textTheme: TextTheme(title: AppBarTextStyle)
        )
      )
    );
  }
}