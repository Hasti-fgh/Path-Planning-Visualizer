<?php get_header(); ?>

<main id="main-content">
    <div class="container">
        <?php
        if ( have_posts() ) :
            while ( have_posts() ) :
                the_post();
                ?>
                <article <?php post_class(); ?>>
                    <h1><?php the_title(); ?></h1>
                    <div class="entry-content">
                        <?php the_content(); ?>
                    </div>
                </article>
                <?php
            endwhile;
        else :
            ?>
            <p><?php esc_html_e( 'No content found.', 'club-bar-theme' ); ?></p>
            <?php
        endif;
        ?>
    </div>
</main>

<?php get_footer(); ?>
