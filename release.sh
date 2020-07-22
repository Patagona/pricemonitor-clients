#!/bin/bash
# This script releases a new version of pricemonitor-clients.
# It first creates a draft release, attaches artifacts and then publish the release.
# Make sure to set the variables GITHUB_TOKEN and VERSION when using it.

GITHUB_ORGANIZATION=Patagona
GITHUB_REPO=pricemonitor-clients

COMMON_PARAMETERS="--user ${GITHUB_ORGANIZATION} --tag ${API_VERSION} --repo ${GITHUB_REPO}"
RELEASE_DIR=tmp
ghr=$RELEASE_DIR/github-release

mkdir -p $RELEASE_DIR
if [ ! -f "$ghr" ]; then
  wget https://github.com/github-release/github-release/releases/download/v0.8.1/linux-amd64-github-release.bz2 -O $RELEASE_DIR/github-release.bz2
  bunzip2 $RELEASE_DIR/github-release.bz2
  chmod +x $ghr
fi

echo "Creating release for version $API_VERSION"
$ghr release ${COMMON_PARAMETERS} --name ${API_VERSION}
