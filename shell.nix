{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python3.withPackages(ps: with ps; [ 
    pip
    pytest
    numpy
    tabulate
     ]);
  
in
pkgs.mkShell {
  packages = with pkgs; [ 
    pythonEnv
    ];

  shellHook = ''
    echo "Python dev shell started"
  '';

}