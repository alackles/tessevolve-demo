/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports) {

	/* global AFRAME THREE */

	if (typeof AFRAME === 'undefined') {
	  throw new Error('Component attempted to register before AFRAME was available.');
	}

	/**
	 * Point component for A-Frame.
	 */
	AFRAME.registerComponent('sphere', {
	  schema: {
        radius: {
			type: 'number',
			default: 1
		},
	    color: {
	      type: 'color',
	      default: '#888'
	    },
	    perspective: {
	      type: 'boolean',
	      default: false
	    }
	  },

	  /**
	   * Set if component needs multiple instancing.
	   */
	  multiple: true,

	  /**
	   * Called once when component is attached. Generally for initial setup.
	   */
	  init: function () {
	    // Create geometry.
	    this.geometry = new THREE.SphereGeometry({
			radius: this.data.radius,
			widthSegments: 32,
			heightSegments: 32
		});
	    this.geometry.vertices.push(new THREE.Vector3(0, 0, 0));
	    // Create material.
	    this.material = new THREE.MeshLambertMaterial({
	      color: this.data.color,
	    });
	    // Create mesh.
	    this.spheres = new THREE.Mesh(this.geometry, this.material);
	    // Set mesh on entity.
	    this.el.setObject3D('mesh', this.spheres);
	  },

	  setPoints: function (spheres) {
	    this.geometry = new THREE.SphereGeometry();
	    var vertices = this.geometry.vertices;
	    spheres.forEach(function (sphere) {
	      vertices.push(new THREE.Vector3(sphere[0], sphere[1], sphere[2]));
	    });
	    // Create mesh.
	    this.spheres = new THREE.Mesh(this.geometry, this.material);
	    // Set mesh on entity.
	    this.el.setObject3D('mesh', this.spheres);
	  },

	  /**
	   * Called when a component is removed (e.g., via removeAttribute).
	   * Generally undoes all modifications to the entity.
	   */
	  remove: function () {
	    this.el.removeObject3D('mesh');
	  }

	});

	AFRAME.registerPrimitive('a-sphere', {
	  defaultComponents: {
	    sphere: {}
	  },
	  mappings: {
	    color: 'sphere.color',
	    radius: 'sphere.radius',
	    perspective: 'sphere.perspective'
	  }
	});


/***/ }
/******/ ]);