use regex::Regex;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("day1.txt")?;
    let reader = BufReader::new(file);
    let mut digits: Vec<char> = Vec::new();
    let mut twoDigitStr: String = "".to_string();
    let mut theTotal: i32 = 0;

    for line in reader.lines() {
        let val = line.unwrap();
        println!("{}", val);
        //println!("{}", chr);
        let re = Regex::new(r"\d").unwrap();
        //let text = "123";
        //let caps = re.captures(val.as_str()).unwrap();
        for cap in re.captures_iter(val.as_str()) {
            let new_val = cap.get(0).unwrap().as_str();
            println!("new_val: {}", new_val);
            digits.push(new_val.chars().next().expect("Empty?"));
            
        }
        twoDigitStr.push(digits[0]); 
        twoDigitStr.push(digits[digits.len()-1]);
        //println!("{}", twoDigitStr);
        let twoDigitInt = twoDigitStr.parse::<i32>().unwrap();
        println!("twoDigitInt: {}", twoDigitInt);
        
        theTotal += twoDigitInt;

        // Reset variables
        twoDigitStr = "".to_string();
        digits = Vec::new();
        
    }

    println!("Total: {}", theTotal);

    Ok(())
}