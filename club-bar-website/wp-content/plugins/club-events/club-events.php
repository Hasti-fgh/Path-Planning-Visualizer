<?php
/**
 * Plugin Name: Club Events & Reservations
 * Description: Manage club events and handle reservations
 * Version: 1.0.0
 * Author: Your Club
 * License: GPL v2 or later
 */

// Prevent direct access
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Create reservations table on plugin activation
function club_events_activate() {
    global $wpdb;
    
    $table_name = $wpdb->prefix . 'club_reservations';
    $charset_collate = $wpdb->get_charset_collate();
    
    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        name varchar(100) NOT NULL,
        email varchar(100) NOT NULL,
        phone varchar(20) NOT NULL,
        event_id mediumint(9) NOT NULL,
        guests int(11) NOT NULL,
        message text,
        status varchar(20) DEFAULT 'pending',
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY  (id)
    ) $charset_collate;";
    
    require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
    dbDelta( $sql );
}
register_activation_hook( __FILE__, 'club_events_activate' );

// Handle reservation form submission
function club_events_handle_reservation() {
    global $wpdb;
    
    if ( $_SERVER['REQUEST_METHOD'] === 'POST' && isset( $_POST['email'], $_POST['name'], $_POST['phone'], $_POST['event'], $_POST['guests'] ) ) {
        
        $table_name = $wpdb->prefix . 'club_reservations';
        
        $name = sanitize_text_field( $_POST['name'] );
        $email = sanitize_email( $_POST['email'] );
        $phone = sanitize_text_field( $_POST['phone'] );
        $event_id = intval( $_POST['event'] );
        $guests = intval( $_POST['guests'] );
        $message = isset( $_POST['message'] ) ? sanitize_textarea_field( $_POST['message'] ) : '';
        
        if ( $name && $email && $phone && $event_id && $guests ) {
            $wpdb->insert(
                $table_name,
                array(
                    'name' => $name,
                    'email' => $email,
                    'phone' => $phone,
                    'event_id' => $event_id,
                    'guests' => $guests,
                    'message' => $message,
                    'status' => 'pending'
                )
            );
            
            // Send confirmation email
            club_events_send_confirmation_email( $email, $name, $guests );
        }
    }
}
add_action( 'wp_loaded', 'club_events_handle_reservation' );

// Send confirmation email
function club_events_send_confirmation_email( $email, $name, $guests ) {
    $subject = 'Reservation Confirmation - ' . get_bloginfo( 'name' );
    $message = "
    <html>
        <body>
            <h2>Reservation Confirmed!</h2>
            <p>Hi " . esc_html( $name ) . ",</p>
            <p>Thank you for your reservation for " . intval( $guests ) . " guest(s).</p>
            <p>We've received your reservation and will contact you shortly to confirm the details.</p>
            <p>Best regards,<br>" . get_bloginfo( 'name' ) . "</p>
        </body>
    </html>";
    
    $headers = array( 'Content-Type: text/html; charset=UTF-8' );
    wp_mail( $email, $subject, $message, $headers );
}

// Add admin menu for reservations
function club_events_admin_menu() {
    add_submenu_page(
        'edit.php?post_type=event',
        'Reservations',
        'Reservations',
        'manage_options',
        'club_reservations',
        'club_events_reservations_page'
    );
}
add_action( 'admin_menu', 'club_events_admin_menu' );

// Display reservations page
function club_events_reservations_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'club_reservations';
    
    $reservations = $wpdb->get_results( "SELECT * FROM $table_name ORDER BY created_at DESC" );
    
    ?>
    <div class="wrap">
        <h1>Club Reservations</h1>
        <table class="wp-list-table widefat fixed striped">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Guests</th>
                    <th>Status</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                <?php
                foreach ( $reservations as $reservation ) {
                    ?>
                    <tr>
                        <td><?php echo esc_html( $reservation->name ); ?></td>
                        <td><?php echo esc_html( $reservation->email ); ?></td>
                        <td><?php echo esc_html( $reservation->phone ); ?></td>
                        <td><?php echo intval( $reservation->guests ); ?></td>
                        <td><span class="badge"><?php echo esc_html( $reservation->status ); ?></span></td>
                        <td><?php echo esc_html( $reservation->created_at ); ?></td>
                    </tr>
                    <?php
                }
                ?>
            </tbody>
        </table>
    </div>
    <?php
}
