#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:).[0-9a-zA-Z]*|(?<=to:).[0-9]*|-?[0-9]:-?[0-9]:-?[0-9]:-?[0-9]:-?[0-9]/).join(",")
