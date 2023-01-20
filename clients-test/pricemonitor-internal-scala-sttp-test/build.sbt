scalaVersion := "2.13.0"
name := "pricemonitor-internal-scala-sttp-test"
organization := "patagona"
version := "1.0"

libraryDependencies += "org.scala-lang.modules" %% "scala-parser-combinators" % "2.1.1"
libraryDependencies += "com.softwaremill.sttp.client" %% "async-http-client-backend-future" % "2.2.9"
libraryDependencies += "org.scalactic" %% "scalactic" % "3.2.15"
libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.15" % "test"

lazy val client = ProjectRef(file("../../clients/pricemonitor-internal-scala-sttp"), "client")
lazy val root = Project("root", file(".")) dependsOn (client)
