version := "0.0.6369"
name := "pricemonitor-client-internal-sttp"
organization := "patagona"

scalaVersion := "2.13.0"

crossScalaVersions := Seq(scalaVersion.value, "2.12.10",  "2.11.12")

libraryDependencies ++= Seq(
  "com.softwaremill.sttp.client" %% "core" % "2.2.9",
  "com.softwaremill.sttp.client" %% "json4s" % "2.2.9",
  "org.json4s" %% "json4s-jackson" % "3.6.7",
  // test dependencies
  "org.scalatest" %% "scalatest" % "3.0.8" % Test,
  "junit" % "junit" % "4.13" % "test"
)

scalacOptions := Seq(
  "-unchecked",
  "-deprecation",
  "-feature"
)

publishArtifact in (Compile, packageDoc) := false
lazy val client = (project in file("."))


publishTo := {
  Some(
    Resolver
      .url("Patagona S3 bucket", url("s3://patagona.repository/build_artifacts/master"))(Resolver.ivyStylePatterns)
  )
}

publishMavenStyle in ThisBuild := false
