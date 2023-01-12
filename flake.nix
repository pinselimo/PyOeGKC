{
  description = "Converter for Austrian municipality codes";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      pyOeGKC = pkgs.python3Packages.buildPythonPackage rec {
                  name = "pyoegkc";
                  src = ./.;
                  propagatedBuildInputs = [ ];
                };
      in {
      packages.default = pyOeGKC;
    });
}
