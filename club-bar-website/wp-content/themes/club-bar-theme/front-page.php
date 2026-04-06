<?php get_header(); ?>

<!-- Hero Section -->
<section class="hero">
    <video autoplay muted loop>
        <source src="<?php echo get_template_directory_uri(); ?>/assets/hero-video.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <h1><?php bloginfo( 'name' ); ?></h1>
        <p><?php bloginfo( 'description' ); ?></p>
        <a href="#events" class="cta-button">View Upcoming Events</a>
    </div>
</section>

<main id="main-content">
    <div class="container">
        <!-- About Section -->
        <section class="about">
            <div class="about-content">
                <h2>About Us</h2>
                <p>Welcome to the ultimate nightlife destination. Experience world-class entertainment, premium drinks, and unforgettable nights with the hottest DJs in the industry.</p>
                <p>Our state-of-the-art venue features cutting-edge sound systems, stunning visual effects, and a vibrant atmosphere that keeps guests coming back for more.</p>
            </div>
            <div class="about-image">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/about-image.jpg" alt="About Us">
            </div>
        </section>

        <!-- Upcoming Events Section -->
        <section class="events-section" id="events">
            <h2>Upcoming Events</h2>
            <div class="events-grid">
                <?php
                $events = new WP_Query( array(
                    'post_type' => 'event',
                    'posts_per_page' => 6,
                    'orderby' => 'meta_value',
                    'meta_key' => 'event_date',
                    'order' => 'ASC',
                ) );

                if ( $events->have_posts() ) :
                    while ( $events->have_posts() ) :
                        $events->the_post();
                        $event_date = get_post_meta( get_the_ID(), 'event_date', true );
                        $dj_name = get_post_meta( get_the_ID(), 'dj_name', true );
                        ?>
                        <div class="event-card">
                            <div class="event-date"><?php echo esc_html( $event_date ); ?></div>
                            <h3 class="event-title"><?php the_title(); ?></h3>
                            <p class="event-dj">DJ: <?php echo esc_html( $dj_name ); ?></p>
                            <p class="event-description"><?php echo wp_trim_words( get_the_content(), 20 ); ?></p>
                            <button class="reserve-button" onclick="scrollToReservation()">Make a Reservation</button>
                        </div>
                        <?php
                    endwhile;
                    wp_reset_postdata();
                else :
                    echo '<p>No upcoming events scheduled.</p>';
                endif;
                ?>
            </div>
        </section>

        <!-- Reservation Form -->
        <section class="reservation-form" id="reservation">
            <h3>Make a Reservation</h3>
            <form method="POST" action="">
                <div class="form-group">
                    <label for="name">Full Name *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email Address *</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number *</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                <div class="form-group">
                    <label for="event">Select Event *</label>
                    <select id="event" name="event" required>
                        <option value="">-- Choose an Event --</option>
                        <?php
                        $events = new WP_Query( array(
                            'post_type' => 'event',
                            'posts_per_page' => -1,
                        ) );

                        if ( $events->have_posts() ) :
                            while ( $events->have_posts() ) :
                                $events->the_post();
                                ?>
                                <option value="<?php the_ID(); ?>"><?php the_title(); ?></option>
                                <?php
                            endwhile;
                            wp_reset_postdata();
                        endif;
                        ?>
                    </select>
                </div>
                <div class="form-group">
                    <label for="guests">Number of Guests *</label>
                    <input type="number" id="guests" name="guests" min="1" max="10" required>
                </div>
                <div class="form-group">
                    <label for="message">Special Requests</label>
                    <textarea id="message" name="message"></textarea>
                </div>
                <button type="submit" class="submit-button">Submit Reservation</button>
            </form>
        </section>
    </div>
</main>

<script>
function scrollToReservation() {
    document.getElementById('reservation').scrollIntoView({ behavior: 'smooth' });
}
</script>

<?php get_footer(); ?>
