<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
    <?php wp_body_open(); ?>

    <header>
        <div class="container">
            <div class="header-content">
                <a href="<?php echo home_url(); ?>" class="logo">
                    <?php bloginfo( 'name' ); ?>
                </a>
                <nav>
                    <?php
                    wp_nav_menu( array(
                        'theme_location' => 'primary',
                        'fallback_cb' => 'wp_page_menu',
                        'container' => false,
                    ) );
                    ?>
                </nav>
            </div>
        </div>
    </header>
