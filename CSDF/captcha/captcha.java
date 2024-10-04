import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;

public class captcha {
    private static final char[] CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            .toCharArray();
    private static final int CAPTCHA_LENGTH = 5;
    private static final int IMAGE_WIDTH = 200;
    private static final int IMAGE_HEIGHT = 80;

    public static void main(String[] args) {
        // generate Captcha
        String captcha = generateCaptcha();
        System.out.println("DEBUG: Captcha generated Successfully: " + captcha);

        // generate Image
        boolean image_genered = createCaptchaImage(captcha);
        if (!image_genered) {
            System.out.println("DEBUG: Error generating image");
            return;
        } else {
            System.out.println("DEBUG: Image generated Successfully and saved as captcha.png");
        }

        // verify Captcha and display GUI
        displayGUI(captcha);

        System.out.println("DEBUG: Program terminated");
    }

    // Function to generate Captcha of specified length and return as String
    private static String generateCaptcha() {
        StringBuilder captcha = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < CAPTCHA_LENGTH; i++) {
            captcha.append(CHARACTERS[random.nextInt(CHARACTERS.length)]);
        }

        return captcha.toString();
    }

    // function to generate a captcha image and save as captcha.png file
    private static boolean createCaptchaImage(String captcha) {
        BufferedImage image = new BufferedImage(IMAGE_WIDTH, IMAGE_HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics2D g2d = image.createGraphics();

        // Set background
        g2d.setColor(Color.WHITE);
        g2d.fillRect(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);

        Random random = new Random();
        // Set font
        Font font = new Font("Arial", Font.BOLD, 40);
        g2d.setFont(font);

        // Draw captcha text
        FontMetrics fontMetrics = g2d.getFontMetrics();
        int textWidth = fontMetrics.stringWidth(captcha);
        int x = (IMAGE_WIDTH - textWidth) / 2;
        int y = (IMAGE_HEIGHT - fontMetrics.getHeight()) / 2 + fontMetrics.getAscent();

        for (int i = 0; i < captcha.length(); i++) {
            // get noise in position
            int dx = random.nextInt(0, 10);
            int dy = random.nextInt(-5, 5);

            // random color of character
            g2d.setColor(new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256)));

            // write character on image at position
            g2d.drawString(String.valueOf(captcha.charAt(i)), x + dx, y + dy);
            x += fontMetrics.charWidth(captcha.charAt(i));
        }

        // Add some noise
        g2d.setColor(Color.BLACK);
        for (int i = 0; i < 100; i++) {
            int x1 = random.nextInt(IMAGE_WIDTH);
            int y1 = random.nextInt(IMAGE_HEIGHT);
            int x2 = x1 + random.nextInt(10) - 5;
            int y2 = y1 + random.nextInt(10) - 5;
            g2d.drawLine(x1, y1, x2, y2);
        }

        g2d.dispose();

        // Save the image
        try {
            File output = new File("captcha.png");
            ImageIO.write(image, "png", output);
            return true;
        } catch (IOException e) {
            System.err.println("ERROR : " + e.getMessage());
        }

        return false;
    }

    private static void displayGUI(String Captcha) {
        // create frame
        JFrame f = new JFrame("CAPTCHA");

        // open image from captcha.png
        File file = new File("captcha.png");
        BufferedImage image = null;
        try {
            image = ImageIO.read(file);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // create label
        JLabel label = new JLabel();
        label.setIcon(new ImageIcon(image));
        label.setBounds(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);
        f.getContentPane().add(label);

        // create text field
        JTextField textfield = new JTextField();
        textfield.setBounds(0, IMAGE_HEIGHT, 100, 50);

        // create submit button
        JButton submit = new JButton("Verify");
        submit.setBounds(100, IMAGE_HEIGHT, 100, 50); // x,y,l,w

        // message label
        JLabel message = new JLabel();
        message.setBounds(0, IMAGE_HEIGHT + 100, 100, 100);
        f.getContentPane().add(message);

        // add action listener
        submit.addActionListener(e -> {
            String input = textfield.getText();
            if ((input != null) && input.equals(Captcha)) {
                // show message if captcha is correct in new label
                JOptionPane.showMessageDialog(f, "Captcha verification successful");
            } else {
                // show message if captcha is incorrect in new label
                JOptionPane.showMessageDialog(f, "Captcha verification failed");
            }
        });

        f.getContentPane().add(textfield);
        f.getContentPane().add(submit);
        f.getContentPane().add(message);

        f.setSize(250, 300);// 400 width and 500 height
        f.setLayout(null);// using no layout managers
        f.setVisible(true);// making the frame visible

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

}