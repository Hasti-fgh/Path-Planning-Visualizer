<?php
/**
 * Club Bar Theme Functions
 */

// Register custom post type for events
function club_bar_register_event_post_type() {
    $labels = array(
        'name' => _x( 'Events', 'Post Type General Name', 'club-bar-theme' ),
        'singular_name' => _x( 'Event', 'Post Type Singular Name', 'club-bar-theme' ),
        'menu_name' => _x( 'Events', 'Admin Menu text', 'club-bar-theme' ),
    );

    $args = array(
        'labels' => $labels,
        'public' => true,
        'publicly_queryable' => true,
        'show_ui' => true,
        'show_in_menu' => true,
        'query_var' => true,
        'rewrite' => array( 'slug' => 'event' ),
        'capability_type' => 'post',
        'has_archive' => true,
        'hierarchical' => false,
        'menu_position' => 5,
        'supports' => array( 'title', 'editor', 'author', 'thumbnail', 'excerpt', 'custom-fields' ),
    );

    register_post_type( 'event', $args );
}
add_action( 'init', 'club_bar_register_event_post_type' );

// Register custom post type for DJs
function club_bar_register_dj_post_type() {
    $labels = array(
        'name' => _x( 'DJs', 'Post Type General Name', 'club-bar-theme' ),
        'singular_name' => _x( 'DJ', 'Post Type Singular Name', 'club-bar-theme' ),
        'menu_name' => _x( 'DJs', 'Admin Menu text', 'club-bar-theme' ),
    );

    $args = array(
        'labels' => $labels,
        'public' => true,
        'publicly_queryable' => true,
        'show_ui' => true,
        'show_in_menu' => true,
        'query_var' => true,
        'rewrite' => array( 'slug' => 'dj' ),
        'capability_type' => 'post',
        'has_archive' => true,
        'hierarchical' => false,
        'menu_position' => 6,
        'supports' => array( 'title', 'editor', 'author', 'thumbnail', 'excerpt', 'custom-fields' ),
    );

    register_post_type( 'dj', $args );
}
add_action( 'init', 'club_bar_register_dj_post_type' );

// Load theme styles and scripts
function club_bar_load_scripts() {
    wp_enqueue_style( 'club-bar-style', get_stylesheet_uri() );
    wp_enqueue_script( 'club-bar-script', get_template_directory_uri() . '/js/main.js', array(), '1.0.0', true );
}
add_action( 'wp_enqueue_scripts', 'club_bar_load_scripts' );

// Theme supports
add_theme_support( 'post-thumbnails' );
add_theme_support( 'title-tag' );
add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption' ) );

// Register navigation menu
register_nav_menus( array(
    'primary' => __( 'Primary Menu', 'club-bar-theme' ),
) );
