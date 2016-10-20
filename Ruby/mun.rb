require 'macaddr'

ADDRESSES = {"84:38:35:4a:03:98" => "Raghav"}

def validate
  50.times do | p |
    print "\rValidating your credentials, please wait. #{(2*(p)+1) > 97 ? 100 : (2*(p)+1)}%"
    sleep (0..0.1).step(0.01).to_a.sample
  end
  puts
  if ADDRESSES.include?(Mac.addr)
    puts "Welcome back, #{ADDRESSES[Mac.addr]}!"
  else
    raise <<-HEREDOC
You don't have valid credentials to run this software. \
To proceed, go back to the main download page online \
and register, contact us to make the payment, \
and then download the software again.
    HEREDOC
  end
end

validate

def input(text)
  print text, ' '
  gets.chomp
end

def integer_input(text)
  (input text).to_i
end

loop do
  $stance = (input "What's your stance [f/a]?").downcase
  break if %w(f a).include? $stance
end

country = (input "What's your country?").split.map(&:capitalize).join(' ')

verb1_for = %w(provides presents renders offers lays_out).sample
verb1_agn = %w(provide present render offer lay_out).sample

adj1 = %w(practical workable achievable attainable viable realistic
        sensible reasonable suitable expedient helpful constructive).sample(2).join(' and ')

issue = input "What's the issue?"

reasons = integer_input "How many reasons do you have? (Limit of 4.)"

for_template =
    "\nHonorable chair, fellow delegates, and most esteemed guests, the delegate of #{country} urges all
#{['representatives','member states'].sample} to vote in favor of this resolution, as it clearly #{verb1_for} #{adj1}
solutions to solve the issue of #{issue}.\n"

against_template =
    "\nHonorable chair, fellow delegates, and most esteemed guests, the delegate of #{country} urges all
#{['representatives','member states'].sample} to vote against this resolution, as it fails to #{verb1_agn} #{adj1}
solutions to solve the issue of #{issue}.\n"

tmplt = ($stance == 'f' ? for_template : against_template)

x = (1..reasons).map { | i |
  sc1 = input("Input clause #{i}: Enter your clause/sub-clause/sub-sub-clause, formatted like so: 3/a/iii.").split('/')
  sc1 = "clause #{sc1[0]}#{if sc1[1] then (sc1[2] ? ", sub-clause #{sc1[1]}, sub-sub-clause #{sc1[2]}" : ", sub-clause #{sc1[1]}") end}"
  scq1 = input("Why is this clause/sub-clause/sub-sub-clause #{$stance == 'f' ? 'good' : 'bad'}? Start with 'This clause...'")
  [sc1,scq1]
}

concl = input "Enter a concluding sentence."

def first_clause(x)
  x[0] = "This delegate would like to start by drawing the house's attention to #{x[0][0]}. #{x[0][1]}"
end

def second_clause(x)
  x[1] = "Secondly, this delegate would like to draw the house's attention to #{x[1][0]}. #{x[1][1]}"
end

def third_clause_not_last(x)
  x[2] = "Thirdly, this delegate would encourage all member states to refer to #{x[2][0]}. #{x[2][1]}"
end

def last_clause(x)
  x[-1] = "Lastly, this delegate would like to draw the house's attention to #{x[2][0]}. #{x[2][1]}"
end

print tmplt.gsub(/_/, ' ')

case reasons
  when 1
    first_clause(x)
    print x.join("\n")
  when 2
    first_clause(x)
    second_clause(x)
    print x.join("\n")
  when 3
    first_clause(x)
    second_clause(x)
    last_clause(x)
    print x.join("\n")
  when 4
    first_clause(x)
    second_clause(x)
    third_clause_not_last(x)
    last_clause(x)
    print x.join("\n")
  else
    puts("Maximum of 4 reasons.")
end

puts "\n", concl, "Thank you."
