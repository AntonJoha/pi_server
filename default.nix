{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    python310Full
    python310Packages.pip
    python310Packages.virtualenv
    pythonPackages.tkinter
  ]);
  runScript = "bash";
}).env
